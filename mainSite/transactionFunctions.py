__author__ = 'fangyuew'

from django.http import HttpResponse, HttpResponseServerError
from mainSite.models import *
import json
import logging
log = logging.getLogger(__name__)
from decimal import *

"""
Incoming order Jason object format
{
    order:
    {
        user_id : # (could be null),
        company_id : #,
        items:
        [
            //items may overlap. eg: [{menu_id:3, amount:2}, {menu_id:1, amount:2},{menu_id:3, amount:1}]
            {
                menu_id : #,
                restaurant_id : #,
                amount : #,
                menu_name : str
            },

            ...

        ]
    },

    ...
    ...
}
"""



"""
GenerateBill : calculate total price of a certain order and generate Bill, DON'T STORE IN DATABASE , and return a json object containing result
1) GenerateBillGateway : encode/decode data in json, make necessary validation, raise errors
2) GenerateBill : generate bill data object

Returning Bill Object format
{
    bill:
    {
        total_price : #,
        deliver_address : str ,
        deliver_time : date-time ,
        restaurants : [
            {   restaurant_id : #,
                restaurant_name : str,
                restaurant_address : str,
                price : #,
                items:
                [
                    {
                        menu_id : #,
                        amount : #,
                        menu_name : str
                    },
                    ...
                ]
            },

            ...

        ]
    }
}
"""

def generateBillGateway(raw_data):
    json_data = json.loads(raw_data)
    order={}
    bill={}
    order = json_data['order']
    bill=generateBill(order)
    return json.dumps({'bill':bill})




def generateBill(order):

    log.info("Order Placed:")
    log.info(order)

    user_id = order['user_id']
    company_id = order['company_id']
    items = order['items']

    #user = MyUser.objects.get(user_id)
    company = Company.objects.get(id__exact=company_id)

    #Aggregate Order Items
    rest_map = {}
    for item in items:
        menu_id = item['menu_id']
        menu_name = item['menu_name']
        restaurant_id = item['restaurant_id']
        amount = item['amount']
        if restaurant_id in rest_map:
            log.info("Found existing rest in rest_map, update it")
            restaurant = rest_map[restaurant_id]  #may contain error since restaurant_id is int
            menu_list=restaurant['items']
            for menu in menu_list:
                if menu['menu_id'] == menu_id:
                    menu['amount'] += amount
                    break
            else:   #if not exist
                menu={'menu_id':menu_id, 'amount':amount, 'menu_name':menu_name}
                menu_list.append(menu)
            log.info(rest_map)
        else:
            log.info("Insert new rest into rest_map")
            restaurant={}
            menu={'menu_id':menu_id, 'amount':amount , 'menu_name':menu_name}
            menu_list=[menu]
            restaurant['items']=menu_list
            rest_map[restaurant_id]=restaurant
            log.info(rest_map)

    log.info("Final rest_map:")
    log.info(rest_map)

    #Process Aggregated data and generate information
    getcontext().prec = 2
    restaurants=[]
    total_price = Decimal(0)
    for rest_id in rest_map.keys():
        restaurant={'restaurant_id':rest_id, 'items':rest_map[rest_id]['items']}
        object=Restaurant.objects.get(id__exact=rest_id)
        restaurant['restaurant_name'] = object.name
        restaurant['restaurant_address'] = object.getAddress()

        price = Decimal(0)

        for item in restaurant['items']:
            menu_id = item['menu_id']
            amount = item['amount']
            m_object = Menu.objects.get(id__exact=menu_id)
            price += m_object.price * amount

        total_price +=price
        restaurant['price'] = float(price)
        restaurants.append(restaurant)


    #insert data to bill
    bill = {};
    bill['total_price'] = float(total_price)
    bill['deliver_address'] = company.getAddress()
    bill['deliver_time'] = None #modify this in the future
    bill['restaurants'] = restaurants

    log.info("Bill Generated:")
    log.info(bill)

    return bill


def storeOrder(request):
    return 1


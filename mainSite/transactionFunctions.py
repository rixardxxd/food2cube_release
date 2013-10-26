__author__ = 'fangyuew'

from django.http import HttpResponse, HttpResponseServerError
from mainSite.models import *
import json
import logging
log = logging.getLogger(__name__)
from decimal import *


"""
FaultTransactionException, An exception to denote fault Transaction.
eg. wrong price.
"""
class FaultTransactionException(Exception):
    def __init__(self, message):
        self.message = message



"""
Incoming order Jason object format
{
    user:
    {
        user_id: #
    },

    company:
    {
        company_id: #
    },
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
    result=generateBill(json_data)
    return json.dumps(result)

def generateBill(data):

    log.info("Function generateBill get called:")
    log.info("Incoming Object:")
    log.info(data)

    user_id = data['user']['user_id']
    company_id = data['company']['company_id']
    items = data['order']['items']

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
    result={'bill':bill}

    log.info("Resulting Object:")
    log.info(result)

    return result

"""
placeBill : Take Bill Object, verify correction. If passed, store information in database.
This is supposed to be called after client side contacted Paying Platform ( like PayPal ) and return with a confirmation number
If verification failed (may be an attack), will call a callback function alertFault();

1) placeBillGateway : encode/decode data in json, make necessary validation, raise errors
2) placeBill : store bill data in database, generate order in database for following service

Incoming Object format
{
    user:
    {
        ...
    },

    company:
    {
        ...
    },

    bill:
    {
        ...
    },

    confirmation:
    {
        confirm_number : str,
        message : str
    }
}

Returning Bill Object format:
{
    result:
    {
        status : str,
        message : str
    }
}

"""
def placeBillGateway(raw_data):
    json_data = json.loads(raw_data)
    result=placeBill(json_data)
    return json.dumps(result)

def placeBill(data):

    log.info("Function placeBill get called:")
    log.info("Incoming Object:")
    log.info(data)

    if  verifyBill(data['bill']) is False:
        return alertFault()

    user_id = data['user']['user_id']
    user = MyUser.objects.get(id=user_id)
    company_id = data['company']['company_id']
    company = Company.objects.get(id=company_id)


    total_price=data['bill']['total_price']
    restaurants=data['bill']['restaurants']
    deliver_address=data['bill']['deliver_address']

    #Create Order and OrderLines
    res_id=[]
    res_name=[]
    for restaurant in restaurants:
        res_id.append(restaurant['restaurant_id'])
        res_name.append(restaurant['restaurant_name'])

    myOrder=Order.objects.create(user=user, dest_company=company, deliver_address=deliver_address, message='Test Data')
    myOrder.save()
    myOrder.restaurants=res_id=[]
    myOrder.save()

    for restaurant in restaurants:
        items=restaurant['items']
        for item in items:
            menu=Menu.objects.get(id=item['menu_id'])
            myOrderLine=OrderLine.objects.create(order=myOrder, menu=menu, quantity=item['amount'])
            myOrderLine.save()

    #Create Transaction
    myTrans = Transaction.objects.create(user=user,dest_company=company,total_amount=total_price)
    myTrans.restaurants=res_id
    myTrans.company_name=Company.objects.get(id=company_id).name
    myTrans.restaurant_names="<+>".join(res_name)
    myTrans.save()

    return {'result':{'status':'success', 'message':''}}

def verifyBill(bill):
    total_price_v=Decimal(bill['total_price'])
    total_price=Decimal(0)
    restaurants=bill['restaurants']
    for restaurant in restaurants:
        price_v=Decimal(restaurant['price'])
        price=Decimal(0)
        items=restaurant['items']
        for item in items:
            menu=Menu.objects.get(id__exact=item['menu_id'])
            amount=item['amount']
            price+=menu.price*amount
        if (abs(price_v - price)>0.01):
            return False
        total_price+=price_v
    if (abs(total_price_v-total_price)>0.01):
        return False
    return True

def alertFault():

    return {'result':{'status':'failed', 'message':'Bill information doesn\'t match'}}
from django.http import HttpResponse

from django.shortcuts import render

from mainSite.models import *

from rest_framework import generics

from mainSite.serializers import CompanySerializer,RestaurantSerializer

from food2cube.settings import BASE_DIR

from mainSite.transactionFunctions import *

import logging
log = logging.getLogger(__name__)


class ListCompanies(generics.ListAPIView):

   # model = Company
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class RestaurantAndMenuFromCompany(generics.ListAPIView):

    serializer_class = RestaurantSerializer
    model = Restaurant
    def get_queryset(self):
        company_id = self.kwargs['id']
        company = Company.objects.filter(id = company_id)
        log.info("company_id is %s" %company_id)

        return Restaurant.objects.filter(nearby_company = company)


def landing(request):

    return render(request,'index.html')# Create your views here.
    #return make_response(open('templates/index.html').read())
    #return  send_file(BASE_DIR + 'static/mainSite/app/index.html')


#Prepare Data:
order_object = {
        'user' : {  'user_id' : 1 },
        'company' : {   'company_id' : 1 },
        'order':
            {
                'items':[
                    {   'menu_id':1, 'restaurant_id':1, 'amount':2, 'menu_name':'Kens Fried Chicken'},
                    {   'menu_id':2, 'restaurant_id':1, 'amount':2, 'menu_name':'Kens Fried Duck'},
                    {   'menu_id':1, 'restaurant_id':1, 'amount':3, 'menu_name':'Kens Fried Chicken'},
                ]
            }
    }

def testing(request):

    data = json.dumps(order_object, indent=4)
    #raw_data = request.raw_post_data
    raw_data = data

    #Call out target function
    try:
        #print()
        result1 = generateBillGateway(raw_data)

        result1=json.loads(result1)
        result1['user']={'user_id':1}
        result1['company']={'company_id':1}

        log.info("result1")
        log.info(result1)
        result1=json.dumps(result1)

        result2 = placeBillGateway(result1)
    except KeyError:
        log.info("Malformed Data!!")
        HttpResponseServerError("Malformed data!")

    return HttpResponse(result2)

def testemail(request):

    return 1

    #return precalculateTotalPrice(request)

# def getRestaurantAndMenuFromCompany(request):
#
#     company_name = request.POST['company_name']
#     company = Company.objects.get(name = company_name)
#     restaurants = Restaurant.objects.filter(nearby_company = company)
#     menus = Menu.objects.filter(restaurant = restaurants)
#
#     print(company)
#     print(restaurants)
#
#     return HttpResponse(menus)
# response_data = {}
# response_data['company'] = company
# response_data['restaurant'] = restaurant
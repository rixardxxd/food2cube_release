from django.http import HttpResponse

from django.shortcuts import render

from mainSite.models import Restaurant,Company,Menu

from rest_framework import generics

from mainSite.serializers import CompanySerializer,RestaurantSerializer

from food2cube.settings import BASE_DIR


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
def testing(request):

    return HttpResponse("You're looking at the results of poll.")

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
    # response_data['restaurant'] =





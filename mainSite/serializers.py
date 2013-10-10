from rest_framework import serializers
from mainSite.models import Company,Restaurant,Menu
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','street','city','state','zip_code')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name','ingredients','category')

class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = ('name','phone_number','street','city','state','zip_code','menus')
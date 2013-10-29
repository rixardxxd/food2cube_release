from django.conf.urls import patterns, url, include

from mainSite import views

from mainSite import loginViews

from rest_framework import generics

from mainSite.models import Company,Restaurant

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^$', views.landing, name='landing'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^login/',loginViews.login_user, name='login_user'),
    url(r'^logout/',loginViews.logout_user, name='logout_user'),
    url(r'^signup/',loginViews.signup_user, name='signup_user'),
    url(r'^listrestaurant/(?P<id>[0-9]+)/', views.RestaurantAndMenuFromCompany.as_view(),name='RestaurantAndMenuFromCompany'),
    url(r'^listcompany/', views.ListCompanies.as_view(),name='company-list'),
)

urlpatterns += staticfiles_urlpatterns()
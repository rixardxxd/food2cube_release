from django.conf.urls import patterns, url, include

from mainSite import views

from mainSite import loginViews

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.landing, name='landing'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^login/$',loginViews.login_user, name='login_user'),
    url(r'^logout/$',loginViews.logout_user, name='logout_user'),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),

)


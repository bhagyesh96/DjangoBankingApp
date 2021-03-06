from django.conf.urls import url,include
from django.urls import include, path, re_path  #for django 2
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
app_name = "dash"

urlpatterns = [
    #dash
    url(r'^$',views.IndexView.as_view(),name="index"),
    #dash/2
    path('<int:pk>/',views.DetailView.as_view(),name="detail"),
    #dash/sample,
    url(r'^sample', TemplateView.as_view(template_name="base.html"), name='sample'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/login'}, name='logout'), #benifit of using next is it mooves out of app with help of url
    url(r'^search/?$', views.search, name='search'), # ? shows that url contain query
    #url(r'^sucess/(?P<user_id>[0-9]+)/?$', views.addBalance, name='sucess'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', views.update.as_view(), name='update'), ## its Django 2 syntax
    url(r'^(?P<pk>[0-9]+)/addmoney/?$', views.addBalance, name='addmoney'),
]

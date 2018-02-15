"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from dash import views
app_name = 'bank'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #dash
    url(r'^dash/',include("dash.urls")),
    #login/ -> dash
    #url(r'^login/$', auth_views.login,{'template_name': 'authenticate/login.html/'}, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view()),

    #appjson rest_api
    url(r'^appjson/',views.UserList.as_view()),

    #loan
    url(r'^loan/',include("loan.urls")),

    #mutualunds
    url(r'^mf/',include("mutualfunds.urls")),







]

urlpatterns = format_suffix_patterns(urlpatterns)
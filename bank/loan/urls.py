from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
app_name = "loan"

urlpatterns = [
    #loanindex
    url(r'^$',views.home.as_view(),name="index"),
    #dash/2
        ]

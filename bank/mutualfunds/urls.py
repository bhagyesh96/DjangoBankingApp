from django.conf.urls import url,include
from . import views

app_name = "mf"

urlpatterns = [
    #loanindex
    url(r'^$',views.mfinfo.as_view(),name="index"),
    #dash/2
    url(r'^fd$',views.fdinfo.as_view(),name="fdindex"),
        ]
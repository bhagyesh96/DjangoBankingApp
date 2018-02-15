
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from loan.models import HomeLoan,CarLoan
from dash.models import dashboard
# Create your views here.

class mfinfo(LoginRequiredMixin, generic.ListView):
    template_name = 'mfindex.html'
    context_object_name = 'query'  # full database is stored in data access via for loop but in detail view data with only primary key

    def get_queryset(self):
        return dashboard.objects.all()


class fdinfo(LoginRequiredMixin, generic.ListView):
    template_name = 'fdindex.html'
    context_object_name = 'query'  # full database is stored in data access via for loop but in detail view data with only primary key

    def get_queryset(self):
        return dashboard.objects.all()

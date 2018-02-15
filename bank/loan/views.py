# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from loan.models import HomeLoan,CarLoan
from dash.models import dashboard



class home(LoginRequiredMixin, generic.ListView):
    template_name = 'loanindex.html'
    context_object_name = 'query'  # full database is stored in data access via for loop but in detail view data with only primary key

    def get_queryset(self):
        return dashboard.objects.all()



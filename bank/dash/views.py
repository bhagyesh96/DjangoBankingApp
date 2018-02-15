from django.shortcuts import render
from django.views import generic
from .models import dashboard
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
import json



# Create your views here.


def sample(request):
    result = dashboard.objects.all()
    template = loader.get_template('sample.html')
    context = {'result': result}
    return HttpResponse(template.render(context, request))


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    context_object_name = 'data'  # full database is stored in data access via for loop but in detail view data with only primary key

    def get_queryset(self):
        return dashboard.objects.all()


class DetailView(generic.DetailView, LoginRequiredMixin):
    model = dashboard
    template_name = "detail.html"

    def get_queryset(self):
        return dashboard.objects.filter()  # detail view needs primary key but list view does not need PK
        # it automatically takes primary key from url and ase as an argument in get_querysem
        # no need to pace in argument of filter
        # you can get values in html ny using database name .get_queryset is not necessary it is only for explaination


@login_required
def search(request):
    if request.method == 'GET':
        var = request.GET.get('acno', None)
        # return HttpResponse("Your account no   : " + var)
        query = get_object_or_404(dashboard, pk=var)
        # query =dashboard.objects.filter(pk = var)

    template = loader.get_template('landing.html')
    context = {'query': query, }
    return HttpResponse(template.render(context, request))


class update(generic.UpdateView, LoginRequiredMixin):
    model = dashboard
    template_name = "updateinfo.html"
    fields = ['balance', 'Join_date', 'accountno', 'balance']


@login_required
def addBalance(request, pk):
    var = request.POST['money']
    user = get_object_or_404(dashboard, pk=pk)

    # return HttpResponse(user.balance)
    var = int(var)
    user.balance += var
    user.save()
    return HttpResponseRedirect(reverse('dash:detail', args=(user.accountno,)))

#REST FRAMEWORK

class UserList(APIView):

#get data from app
    def get(self,request):
        user = dashboard.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

#send data to app
    def post(self):
        pass




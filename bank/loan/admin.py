from django.contrib import admin

# Register your models here.
from .models import HomeLoan,CarLoan

admin.site.register(HomeLoan)
admin.site.register(CarLoan)

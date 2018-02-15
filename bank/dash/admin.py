from django.contrib import admin


# Register your models here.
from .models import dashboard,accounts

admin.site.register(dashboard)
admin.site.register(accounts)
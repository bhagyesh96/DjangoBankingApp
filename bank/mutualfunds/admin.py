from django.contrib import admin

# Register your models here.
from .models import mfinfo,FD

admin.site.register(mfinfo)
admin.site.register(FD)


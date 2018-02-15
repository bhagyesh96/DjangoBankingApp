from django.db import models
from dash.models import dashboard

# Create your models here.
class mfinfo(models.Model):
    dashboard = models.ForeignKey(dashboard,on_delete=models.CASCADE)
    SchemeName = models.CharField(max_length=50)
    Unit = models.FloatField(default=0)
    Price = models.FloatField(default=0)

    def __str__ (self):
        return "{} - {} ".format(self.dashboard,self.SchemeName)

class FD(models.Model):
    dashboard = models.ForeignKey(dashboard,on_delete=models.CASCADE)
    Duration = models.FloatField(default=0)
    Investment = models.FloatField(default=0)
    IntrestRate = models.FloatField(default=0)

    def __str__ (self):
        return "{} - {} ".format(self.dashboard,self.Investment)


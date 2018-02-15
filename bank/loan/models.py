from django.db import models
# Create your models here.
from dash.models import dashboard,accounts


class HomeLoan(models.Model):
    dashboard = models.ForeignKey(dashboard,on_delete=models.CASCADE)
    LoanNO = models.IntegerField(primary_key=True,default=0)
    IntrestRate = models.IntegerField(default=8)
    AllotedCredit = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {} - Home Loan".format(self.LoanNO,self.key)

class CarLoan(models.Model):
    dashboard = models.ForeignKey(dashboard,on_delete=models.CASCADE)
    LoanNO = models.IntegerField(primary_key=True,default=0)
    IntrestRate = models.IntegerField(default=8)
    AllotedCredit = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {} - Car Loan".format(self.LoanNO,self.key)



from django.db import models

# Create your models here.
class dashboard(models.Model):
    name = models.CharField(max_length=200,default="xyz")
    accountno = models.IntegerField(default=0,primary_key=True)
    Join_date = models.DateTimeField('date published')
    balance= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class accounts(models.Model):
    dashboard = models.ForeignKey(dashboard, on_delete=models.CASCADE)
    InsurencePolicy = models.IntegerField(default=0)
    MutualFund = models.IntegerField(default=0)
    FixedDeposite = models.IntegerField(default=0)
    loan = models.IntegerField(unique=True,default=0)

    def __str__(self):

            return self.dashboard.name


from django.db import models

# Create your models here.
class customer(models.Model):
    CustomerId	= models.CharField(max_length = 1000,null=True)
    Surname	=models.CharField(max_length = 1000)
    CreditScore	=models.IntegerField()
    Geography	=models.CharField(max_length = 1000)
    Gender	=models.CharField(max_length = 100)
    Age	=models.IntegerField()
    Tenure	=models.IntegerField()
    Balance	=models.DecimalField(max_digits=50,decimal_places=5)
    NumOfProducts	=models.IntegerField()
    HasCrCard	=models.IntegerField()
    IsActiveMember	=models.IntegerField()
    EstimatedSalary=models.DecimalField(max_digits=50,decimal_places=5)
from django.db import models


# Create your models here.

class credit_table(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    phno=models.IntegerField()
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    



from django.db import models

# Create your models here.
class Emp(models.Model):
	name=models.CharField(max_length=50,null=True)
	age=models.IntegerField(null=True)
	salary=models.FloatField(null=True)
	desig=models.CharField(max_length=50,null=True)
	phno=models.IntegerField(null=True)
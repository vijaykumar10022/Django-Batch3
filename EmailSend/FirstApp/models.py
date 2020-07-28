from django.db import models

# Create your models here.
class Eamil(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)


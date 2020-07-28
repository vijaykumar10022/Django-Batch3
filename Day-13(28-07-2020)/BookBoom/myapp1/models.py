from django.db import models

# Create your models here.
class Registration(models.Model):
	name=models.CharField(max_length=50,null=True)
	email=models.EmailField(max_length=30,null=True)
	phno=models.IntegerField(null=True)
	username=models.CharField(max_length=30,null=True)
	password=models.CharField(max_length=30,null=True)
class Mybooks(models.Model):
	bookname=models.CharField(max_length=30,null=True)
	bookauthor=models.CharField(max_length=30,null=True)
	bookcost=models.IntegerField(null=True)
	bookimage=models.ImageField()

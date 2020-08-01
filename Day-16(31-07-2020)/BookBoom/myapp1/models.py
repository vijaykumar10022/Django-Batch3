from django.db import models

# Create your models here.

class Mybooks(models.Model):
	bookname=models.CharField(max_length=30,null=True)
	bookauthor=models.CharField(max_length=30,null=True)
	bookcost=models.IntegerField(null=True)
	bookimage=models.ImageField()

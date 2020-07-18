from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):

	return HttpResponse("<h2>This is My Django project</h2>")

def hello(req):
	name="APSSDC"
	return HttpResponse('Hello Gud Afternoon to All '+name)

def hi(req,sdc):

	return HttpResponse("Hii "+sdc)

def rollno(req,rollno):

	return HttpResponse('My Roll No is :{}'.format(rollno))

def task(req,name,roll):
	print(type(name))
	print(type(roll))
	return HttpResponse("My Name is {} and my roll no is {}".format(name,roll))
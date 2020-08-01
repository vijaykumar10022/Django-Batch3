from django.shortcuts import render,redirect
from myapp1.forms import Myform,Books # Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from BookBoom.settings import EMAIL_HOST_USER
from myapp1.models import Mybooks
from django.contrib.auth.decorators import login_required
def register(request):
	if request.method=="POST":
		data=Myform(request.POST)
		if data.is_valid():
			data.save()
			return redirect('login')
	form=Myform()
	return render(request,'myapp1/register.html',{'form':form})

def home(request):
	return render(request,'myapp1/home.html')
@login_required
def addbook(request):
	if request.POST:
		data=Books(request.POST,request.FILES)
		if data.is_valid():
			data.save()
			return redirect('showbooks')
	form=Books()
	return render(request,'myapp1/addbook.html',{'form':form})

def showbooks(request):
	data=Mybooks.objects.all()
	return render(request,'myapp1/showbooks.html',{'data':data})
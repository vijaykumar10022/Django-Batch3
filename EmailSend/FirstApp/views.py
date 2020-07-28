from django.shortcuts import render
from EmailSend import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import random
from FirstApp.models import Eamil
# Create your views here.
def email(request):
	if request.method=='POST':
		email=request.POST['email']
		subject=request.POST['subject']
		body=request.POST['body']
		sender=settings.EMAIL_HOST_USER
		reciver=email
		send_mail(subject,body,sender,[reciver])
		return HttpResponse("<h2>Please check This Mail</h2> "+email)

	return render(request,'email.html')


def register(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		uname=request.POST['username']
		password=random.randint(100000,999999)
		Eamil.objects.create(first_name=fname,last_name=lname,
			email=email,username=uname,password=password)
		sub="Reg to your login details.."
		body="""Hello {}\n\n this is your Usernaxme: {}\n\n
		your password: {}\n\n """.format(fname,uname,password)
		sender=settings.EMAIL_HOST_USER
		reciver=email
		send_mail(sub,body,sender,[reciver])
		return HttpResponse('Check Your Mail for Login Details')
	return render(request,'register.html')

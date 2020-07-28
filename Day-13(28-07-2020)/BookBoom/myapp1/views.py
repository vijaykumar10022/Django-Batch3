from django.shortcuts import render,redirect
from myapp1.forms import UserForm,Userlogin # Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from BookBoom.settings import EMAIL_HOST_USER
from myapp1.models import Registration
def register(request):
	if request.method=="POST":
		name=request.POST['name']#vijay
		phno=request.POST['phno']#9876541230
		email=request.POST['email']#vijay10022@gmail.com
		#username=vijay41230
		#password=bookboomvijay!@#
		username=name+phno[-5:]
		password="bookboom"+name+"!@#"
		subject="Regarding User Creditionals ....!!!"
		body="Username is ---> "+username +"  password is---> "+password
		sender=EMAIL_HOST_USER
		reciver=email
		send_mail(subject,body,sender,[reciver])
		Registration.objects.create(name=name,phno=phno,email=email,username=username,password=password)
		return redirect('login')
	form=UserForm()
	return render(request,'myapp1/register.html',{'form':form})
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		try:
			if Registration.objects.get(username=username,password=password):
				return redirect('home')
		except Exception:
			return HttpResponse("Wrong Creditionals ...!!!!")
	form=Userlogin()
	return render(request,'myapp1/login.html',{'form':form})
def home(request):
	return render(request,'myapp1/home.html')
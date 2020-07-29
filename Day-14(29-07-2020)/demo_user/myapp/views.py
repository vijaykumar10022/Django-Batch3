from django.shortcuts import render
from myapp.forms import Myform
from django.http import HttpResponse
# Create your views here.

def register(request):
	if request.method=="POST":
		data=Myform(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("Done....")
	form=Myform()
	return render(request,'myapp/register.html',{'form':form})
def home(request):
	return render(request,'myapp/home.html')
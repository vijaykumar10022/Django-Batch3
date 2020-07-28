from django.shortcuts import render

# Create your views here.
def myhome(request):
	return render(request, 'myapp/myhome.html')

def myform(request):
	return render(request, 'myapp/myform.html')

def myform2(request):
	return render(request, 'myapp/myform2.html')

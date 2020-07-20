from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'firstapp/home.html')

def internal(request):
	return render(request, 'firstapp/internal.html')

def external(request):
	return render(request, 'firstapp/external.html')

def add(request):
	return render(request, 'firstapp/add.html')
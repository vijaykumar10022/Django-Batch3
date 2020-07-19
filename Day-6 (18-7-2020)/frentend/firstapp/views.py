from django.shortcuts import render

# Create your views here.
def register(request):
	return render(request, 'firstapp/register.html')

def table(request):
	return render(request, 'firstapp/table.html')
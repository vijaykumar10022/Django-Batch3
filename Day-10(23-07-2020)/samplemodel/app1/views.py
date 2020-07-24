from django.shortcuts import render
from app1.models import Emp
from django.http import HttpResponse
# Create your views here.
def store(request):
	if request.method=="POST":
		name=request.POST['name']
		age=request.POST['age']
		salary=request.POST['salary']
		Emp.objects.create(name=name,age=int(age),salary=float(salary))
		return HttpResponse("<h1>Done</h1>")
		# print(name,age,salary,desig,phno)

	return render(request,'app1/store.html')

def store2(request):
	if request.method=="POST":
		desig=request.POST['desig']
		phno=request.POST['phno']
		Emp.objects.create(desig=desig,phno=int(phno))
		return HttpResponse("<h1>Done</h1>")
		# print(name,age,salary,desig,phno)

	return render(request,'app1/store.html')

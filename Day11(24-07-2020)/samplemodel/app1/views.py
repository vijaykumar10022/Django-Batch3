from django.shortcuts import render,redirect
from app1.models import Emp
from django.http import HttpResponse
# Create your views here.
def store(request):
	if request.method=="POST":
		name=request.POST['name']
		age=request.POST['age']
		salary=request.POST['salary']
		desig=request.POST['desig']
		phno=request.POST['phno']
		Emp.objects.create(name=name,age=int(age),salary=float(salary),desig=desig,phno=int(phno))
		return redirect('/display')
		# print(name,age,salary,desig,phno)

	return render(request,'app1/store.html')

def display(request):
	data=Emp.objects.all()
	return render(request,'app1/display.html',{'info':data})
def delete(request,name):
	data=Emp.objects.get(name=name)
	data.delete()
	return redirect('/display')
def update(request,age):
	data=Emp.objects.get(age=age)
	if request.method=="POST":
		name=request.POST['name']
		age=request.POST['age']
		salary=request.POST['salary']
		desig=request.POST['desig']
		phno=request.POST['phno']
		data.name=name
		data.age=age
		data.salary=salary
		data.desig=desig
		data.phno=phno
		data.save()
		return redirect('/display')
	return render(request,'app1/update.html',{'mydata':data})
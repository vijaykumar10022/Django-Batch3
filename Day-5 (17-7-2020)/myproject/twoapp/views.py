from django.shortcuts import render

# Create your views here.
def d_name(request,name):
	u_name = {'name': name}
	return render(request, 'twoapp/name.html', u_name)

def table(request,num):
	data =[]
	for i in range(1,11):
		td = str(num)+"*"+str(i)+'='+str(num*i)
		data.append(td)
		#print(td)
	return render(request,'twoapp/table.html', {'info':data})


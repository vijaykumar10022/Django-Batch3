from django.shortcuts import render
from django.http import HttpResponse
import random
import qrcode
# Create your views here.
otp=0
def login(request):
    return render(request,'testapp/login.html')

def validate_user(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upassword=request.POST['upassword']
        if uname=="Harideep" and upassword=="apssdc@123":
            rno=random.randint(1000,9999)
            global otp
            otp=rno
            im=qrcode.make("Your otp is: "+str(otp))
            im.save('testapp/static/qrimages/pic1.jpg')
            return render(request,'testapp/qrcode.html')

        else:
            return HttpResponse("Invalid Username or Password")

def validate_otp(request):
    if request.method=="POST":
        uotp=request.POST['uotp']
        if otp==int(uotp):
            return render(request,'testapp/welcome.html')
        else:
            return HttpResponse("Invalid Otp")

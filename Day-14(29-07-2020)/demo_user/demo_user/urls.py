"""demo_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('signin/',LoginView.as_view(template_name='myapp/signin.html'),name="signin"),
    path('logout/',LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
]

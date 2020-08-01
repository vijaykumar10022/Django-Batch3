"""BookBoom URL Configuration

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
from myapp1 import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('login/',LoginView.as_view(template_name='myapp1/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='myapp1/index.html'),name='logout'),
    path('addbook/',views.addbook,name='addbook'),
    path('showbooks/',views.showbooks,name='showbooks'),
]

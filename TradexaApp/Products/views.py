from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Products
# Create your views here.
def Product(request):
    prod_list=Products.objects.all().order_by('-created_date')
    return render(request,'products.html',{'prod_list':prod_list})
def Logout(request):
    auth.logout(request)  
    return redirect('/')          
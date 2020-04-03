from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post
from datetime import datetime,date
# Create your views here.
def user(request):
    posts= Post.objects.all().order_by('-created_date')
    return render(request,'index.html',{'posts':posts})
def CreatePost(request):
    if request.method=='POST':
        user=request.user
        comment=request.POST['comment']
        today = date.today()
        created_date=today.strftime("%Y-%m-%d")
        post=Post.objects.create(user=user,text=comment,created_date=created_date,updated_date=created_date)
        post.save
        posts= Post.objects.all().order_by('-created_date')
        print("post created",user)
    return render(request,'index.html',{'posts':posts})   
def Registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                print('user taken')
                messages.info(request,'user already taken')
                return redirect('Registration')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'Invalid user')
                return redirect('Registration')
            else:    
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save()
                print('usercreated')
        
        else:
            print('password not matching')
            messages.info(request,'Password not same')
            return redirect('Registration')
        return redirect('/')
    else:
        return render(request,'register.html')
def Login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
                auth.login(request,user)
                return redirect('/')
        else:    
                   messages.info(request,'Invalid user')
                   return redirect('Login')
    else:
        return render(request,'login.html')       
def Logout(request):
    auth.logout(request)  
    return redirect('/')      
  

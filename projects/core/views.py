from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('upload')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')

def signupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        print(username,password,confirm_password)
        if password==confirm_password:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            messages.success(request,'User created successfully')
        else:
            messages.info(request, 'Password is not matching')
    return render(request, 'signup.html')
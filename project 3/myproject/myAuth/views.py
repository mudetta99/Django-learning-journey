from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import check_password 

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password  = request.POST['confirm_password ']

        if password == confirm_password:
            user = MyAuth.objects.create(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")


    return render(request, 'myAuth/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = MyAuth.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                messages.success(request, "Login Successfully")
                return redirect('courses')
            else:
                messages.error(request, "Invlaid Credentials")

        except MyAuth.DoesNotExist :
            messages.error(request, "Invlaid Credentials")

    return render(request, 'myAuth/login.html')





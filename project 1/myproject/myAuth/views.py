from django.shortcuts import render

def register(request):
    return render(request, 'myAuth/register.html')

def login(request):
    return render(request, 'myAuth/login.html')

def logout(request):
    return render(request, 'myAuth/logout.html')
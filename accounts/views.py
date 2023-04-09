from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from .models import Agent
# Create your views here.
User=get_user_model()
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email = request.POST.get('email')
        number= request.POST.get('number')
        user=User.objects.create_user(username=username,password=password,email=email,phone_number=number)
        login(request,user)
        return redirect('index')

    return render(request,'location/signup.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('index')

    return render(request,'location/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def agent(request, variable):
    return render(request, f"location/agent-{variable}.html",context={'agents':Agent.objects.all()})
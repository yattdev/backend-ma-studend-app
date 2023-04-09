from django.shortcuts import render,redirect,get_object_or_404
from .models import Apartment
from accounts.models import Agent
# Create your views here.

def index(request):
    return render(request,'location/index.html',context={'apartments':Apartment.objects.all(),'agents':Agent.objects.all()})
def detail(request,slug):
    apartment=get_object_or_404(Apartment,slug=slug)
    return render(request,'location/detail.html',context={'apartment':apartment})
def about(request):
    return render(request,'location/about.html')

def blog(request,variable):
    return render(request,f"location/blog-{variable}.html")

def property(request,variable):
    return render(request,f'location/property-{variable}.html')
def contact(request):
    return render(request,'location/contact.html')

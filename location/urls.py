from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('apartment/<str:slug>',detail,name='apartment'),
    path('about/',about,name='about'),
    path('blog/<str:variable>',blog,name='blog'),
    path('property/<str:variable>',property,name='property'),
    path('contact',contact,name='contact')
]
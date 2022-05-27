from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def home(request):
    context={"name":"Rahul"}


    return render(request,'home.html')
    
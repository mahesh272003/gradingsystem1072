from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'projectlogin.html')

def practice(request):
    return render(request,'practice.html')


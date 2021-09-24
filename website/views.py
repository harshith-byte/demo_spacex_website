from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    return render(request,'website/welcome.html')

def registers(request):
    form=createuser()

    if request.method=='POST':
        form=createuser(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request,'user created for '+user)
            return redirect('signin')

    content={'form':form}
    return render(request,'website/register.html',content)

def signin(request):
    form=createuser()
    content={'form':form}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else :
            messages.info(request,'username or password is incorrect')
            
    
    return render(request,'website/Sign-in.html',content)

def logoutuser(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def main(request):
    return render(request,'website/main.html')

@login_required(login_url='signin')
def about(request):
    return render(request,'website/about.html')

@login_required(login_url='signin')
def images(request):
    return render(request,'website/images.html')

@login_required(login_url='signin')
def news(request):
    return render(request,'website/news.html')

@login_required(login_url='signin')
def starlink(request):
    if request.method=='POST':
        form=starlinkregister(request.POST)
        form.save()
        user =form.cleaned_data.get('id')
        messages.success(request,'order has been placed for id '+user)
    return render(request,'website/starlink.html')

@login_required(login_url='signin')
def missions(request):
    return render(request,'website/missions.html')
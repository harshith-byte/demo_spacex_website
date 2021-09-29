from website.serializers import registerSerializer
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

from django.http import HttpResponse, response
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
    if request.method=='POST':
        return Response({"data":"hi"})
    return render(request,'website/signin.html')

def auth(request):

    return Response({})

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
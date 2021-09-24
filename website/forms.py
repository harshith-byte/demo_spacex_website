from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields 

from .models import *

class createuser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class signinuser(UserCreationForm):
    class Meta:
        models=User
        fields=['username','password1']
class starlinkreg(UserCreationForm):
    class Meta:
        models=starlinkregister
        fields=['username','email','location']
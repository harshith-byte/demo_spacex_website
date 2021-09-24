from django.db import models

# Create your models here.
class register(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

class starlinkregister(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=100)
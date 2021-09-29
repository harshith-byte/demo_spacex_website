
from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.registers,name='register'),
    path('signin/',views.signin,name='signin'),
    path('auth/',views.auth,name='auth'),
    path('lohoutuser/',views.logoutuser,name='logoutuser'),
    path('main/',views.main,name='main'),
    path('about/',views.about,name='about'),
    path('images/',views.images,name='images'),
    path('news/',views.news,name='news'),
    path('starlink/',views.starlink,name='starlink'),
    path('missions/',views.missions,name='missions'),
]
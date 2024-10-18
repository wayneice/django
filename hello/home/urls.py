
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contacts",views.contacts,name='contacts')
    #if this is a blank path it goes to views index function 
]
# path("Registration1",views.Registration1,name='Registration1'),

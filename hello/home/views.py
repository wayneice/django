from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
#render is used to render template

def index(request):
    context={'variable':"this is sent"}
    return render(request,"index.html",context)
# this is used to return a string HttpResponse
def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is the about page ")
def services(request):
    return render(request,"services.html")
def contacts(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name  ,email=email, desc=desc ,phone=phone ,date=datetime.today())
        contact.save()
        messages.success(request, "Your form was sucessfully submitted.") 
    return render(request,"contacts.html")
from django.db.models import Q
from django.shortcuts import render,HttpResponse

def homefunction(request):
    return render(request , "index.html")
def aboutfunction(request):
    return render(request , "about.html")
def loginfunction(request):
    return render(request , "login.html")
def contactfunction(request):
    return render(request , "contact.html")

def facultylogin(request):
    return render(request,"facultylogin.html")
def studentlogin(request):
    return render(request,"studentlogin.html")
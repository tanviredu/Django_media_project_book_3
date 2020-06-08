## this is the core library
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.template import Context

## Adding the user auth functionality
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
###

## database model
from .models import  Article
from django.contrib.auth.models import User

## form
from .forms import ArticleForm
from .forms import MyRegistrationForm


def auth_login(request):
    c = {}
    return render(request,'article/auth/login.html',c)

def auth_view(request):
    ## take the username
    # and password
    ## either it gets username
    ## or an empty string
    username = request.POST.get('username',' ')
    password = request.POST.get('password',' ')

    #print(username)
    #print(password)
    ## authenticate the user
    ## must strip the data before passing
    user_object = authenticate(username=str.strip(username),password =str.strip(password))
    if user_object is not None:
        login(request,user_object)
        return redirect('/accounts/loggedin')
    else:
        return redirect('/accounts/invalid')


def logged_in(request):
    ## after login this thing will come
    username = request.user.username
    print("[+] Status : successfull Login ")
    return HttpResponse(username + " you are logged in")
    #return render('loggedin.html','username':username)

def invalid_login(request):
    print("[-] Status : Invalid Login ")
    return HttpResponse("Invalid Login")

def logged_out(request):
    logout(request)
    print("[+] Status : successfull Logout ")
    return HttpResponse("you are logged out")


def register_user(request):
    if request.method == "POST":

        # if the form is submitted
        myform = MyRegistrationForm(request.POST)
        ## check the form is valid
        if myform.is_valid():
            myform.save()
            print("[+] Status : successfull registration ")
            return HttpResponse("registration successfull")

    ## if the form is not submitted
    ## then show the form
    ## creating dictionary the hard way
    else:
        myform = MyRegistrationForm()
    return render(request,'article/auth/register.html',{'form':myform})

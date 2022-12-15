from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import User, UserCreationForm
# Create your views here.

from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login


from .models import *
from .forms import CreateUserForm


def say_hello(request):
    return render (request,'hello.html',{'name':request.User})


def login_request(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            print(request.user.groups.all()[0]=='seller')
            if request.user.groups.all()[0].name == 'seller':
                return redirect('core:Seller')
            else:
                return redirect('core:Item-list')
            # if request.user.groups.all()[0]

    return render(request,'login.html',context)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("start:login")

def signup(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'signup.html',context)

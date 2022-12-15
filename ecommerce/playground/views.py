from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login


from .models import *
from .forms import CreateUserForm


def say_hello(request):
    return render (request,'hello.html',{'name':user.name})


def login_request(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect('/hello/')




    return render(request,'login.html',context)

def signup(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'signup.html',context)

from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

import bcrypt

# Create your views here.

def index(request):
    if 'id' in request.session.keys():
        return redirect('users:success')
    else:
        return render(request,"users/index.html")


def register(request):
    errors = User.objects.validate(request)
    if (errors):
        print("invalid input")
        return redirect('users:index')
    else:
        #hash password
        hash_password = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt())
        print (hash_password)
        #create user
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], birthdate=request.POST['birthdate'], password=hash_password)
        user = User.objects.filter(email=request.POST['email'])
        request.session['id'] = user[0].id
    return redirect('users:success')

def login(request):
    email = request.POST['email']
    password = request.POST['pwd']
    user = User.objects.filter(email=email)
    if len(user) == 0:
        messages.error(request,"User not recognized")
        return redirect('users:index')
    else:
        if ( bcrypt.checkpw(password.encode(), user[0].password.encode()) ):
            print ('password matches')
            request.session['id'] = user[0].id
            return redirect('users:success')
        else:
            messages.error(request,'Invalid password.')
            return redirect('users:index')

def success(request):
    if 'id' in request.session.keys():
        return redirect('sports:dashboard')
    else:
        return redirect('users:index')

   
    
def logout(request):
    request.session.clear()
    return redirect('users:index')
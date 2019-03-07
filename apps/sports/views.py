from django.shortcuts import render, redirect
from django.contrib import messages

from ..users.models import User


def index(request):
    return redirect('sports:dashboard')


def dashboard(request):
    if 'id' not in request.session.keys():
        return redirect('users:index')

    else:

        return render(request,"sports/index.html")

        

    
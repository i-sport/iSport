from django.shortcuts import render, redirect
from django.contrib import messages

from ..users.models import User


def index(request):
    if 'id' not in request.session.keys():
        return redirect('users:index')
    else:
        return redirect('events:dashboard')


def dashboard(request):
    user_id = request.session['id']

    user = User.objects.get(id=user_id)
    context = {
        "user": user
    }
    return render(request,'events/dashboard.html', context)

        
def new(request):
    return render(request, 'events/new.html')
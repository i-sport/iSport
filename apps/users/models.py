from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from datetime import datetime
from django.utils import timezone
import datetime

# Create your models here.

class UserManager(models.Manager):
    def validate(self, request):
        errors = False
        
        # validations here
        if len(request.POST['first_name']) < 2:
            messages.error(request,'First name must be at least 2 characters!')
            errors = True  
        if not request.POST['first_name'].isalpha():
            messages.error(request,"First name should contain alpha characters only")
            errors = True
        if len(request.POST['last_name']) < 2:
            messages.error(request,'Last name must be at least 2 characters!')
            errors = True
        if not request.POST['last_name'].isalpha():
            messages.error(request,"Last name should contains alpha characters only")
            errors = True
        if len(request.POST['email']) < 1:
            messages.error(request,'Email can not be empty!')
            errors = True
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.error(request,'Invalid Email Address!')
            errors = True
        if len(request.POST['pwd']) < 8:
            messages.error(request,'Password should be at least 8 characters!')
            errors = True
        if request.POST['pwd'] != request.POST['conf_pwd']:
            messages.error(request,'Password does not match password confirmation')
            errors = True
        #validate email already in use
        user = User.objects.filter(email=request.POST['email'])
        if len(user) != 0:
            messages.error(request,"This email has already been registered")
            errors = True

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthdate = models.DateTimeField(default="1981-08-31")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name,self.last_name)
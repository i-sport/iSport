from django.db import models
from ..users.models import User
# Create your models here.

class EventManager(models.Manager):
  pass


class Event(models.Model):
  name = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  date = models.DateTimeField()
  attendees= models.ManyToManyField(User, related_name = "attended_events")
  creator= models.ForeignKey(User, related_name = "events")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)            
  objects= EventManager()


  
class Message(models.Model):
	message = models.TextField()
	user = models.ForeignKey(User, related_name='u_messages')
	event = models.ForeignKey(Event, related_name='e_messages')
	created_at = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now=True)
	objects = EventManager()

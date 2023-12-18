from datetime  import date
from django.db import models
from sys import modules
from turtle import title
import uuid

# Create your models here.
class module(models.Model):
    title = models.CharField(max_length= 250)
    Desc = models.TextField(null= True, blank= True)
    module_leader = models.CharField(max_length= 250, null=True)
    module_credits= models.IntegerField()
    module_link = models.CharField(max_length= 1000, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
     return self.title

class comment(models.Model):
    rate_type = (
        ('up','up_vote'),
        ('down', 'down_vote')
    )
    # owner=
    module = models.ForeignKey(module, on_delete=models.CASCADE,)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, choices=rate_type)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
       return self.name

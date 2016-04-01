
# Importing 'models' from the 'django.db'

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Here I created the models in my domain, which are: Item, Location, User and SharedItem
# For each model/class I have specified the fields that need to exist, as demonstrated below

class Item(models.Model):
    # I have created a primary key in the beginning of each model/class/table, just as shown in the next line below
    id = models.AutoField(primary_key = True)    
    name=models.CharField(max_length=96, unique=True, blank=True)
    category=models.CharField(max_length=96, unique=True, blank=True)
    description=models.CharField(max_length=96, unique=True, blank=True)
    
class Location(models.Model):
    id = models.AutoField(primary_key = True)
    address=models.CharField(max_length=96, unique=True, blank=True)
	# Specifying the latitude and longitude fields to to be decimal fields of maximum 10 digits and 6 decimal places
    lat=models.DecimalField(max_digits=10, decimal_places=6)
    lng=models.DecimalField(max_digits=10, decimal_places=6)

class User(models.Model):
    id = models.AutoField(primary_key = True)    
    username=models.CharField(max_length=96, unique=True, blank=True)
    firstname=models.CharField(max_length=96, unique=True, blank=True)
    surname=models.CharField(max_length=96, unique=True, blank=True)
    email=models.CharField(max_length=96, unique=True, blank=True)
    phone=models.IntegerField(unique=True, blank=True)
    password=models.CharField(max_length=96, unique=True, blank=True)

class SharedItem(models.Model):
    id = models.AutoField(primary_key = True)
    trade_type=models.CharField(max_length=96, unique=True, blank=True)
    trade_status=models.CharField(max_length=96, unique=True, blank=True)
    # I include a timestamp with the SharedItem record as it gets creates, which is generated automatically without requiring input from the user
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
	# I have put foreign keys in the 'SharedItem' table (below) that refer to each of the other tables
    item_id=models.ForeignKey(Item)
    location_id=models.ForeignKey(Location)
    user_id=models.ForeignKey(User)
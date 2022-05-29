from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import email

'''
note: this is a donor table , we are saving user all info in db.
'''
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=255, unique=True, default="")
    phone = models.CharField(max_length=50, unique=True, default="")
    address = models.CharField(max_length=255,default="")
    adhar_card = models.CharField(max_length=255, unique=True, default="")
    pan_card = models.CharField(max_length=255, unique=True, default="")
    upline_id = models.CharField(max_length=255, default="")
    payment_status = models.CharField(max_length=255, default=False)
    user_plan = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.name
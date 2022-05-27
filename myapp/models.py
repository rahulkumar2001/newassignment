from django.db import models

import email
from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    password=models.CharField(max_length=50,default="")
    
    adhaar_card = models.CharField(max_length=50,default="")
    pan_card = models.CharField(max_length=50,default="")
    upline_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name
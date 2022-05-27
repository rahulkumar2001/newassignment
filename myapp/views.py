from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.models import Donor
import random
from django.http import Http404
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
 
def index(request):
  return HttpResponse("Hello test api")


class Donordata(APIView):
  def post(self, request):
    # try:
    name = request.data['name']
    email = request.data['email']
    phone = request.data['phone']
    address = request.data['address']
    adhaar_card=request.data['adhaar_card']
    pan_card=request.data['pan_card']

    upline_id = request.data['upline_id']
    random_num=random.randint(1,6)
    add_str="bbwf00"
    
    
    data = Donor.objects.create(name=name, email=email,phone=phone,address=address, upline_id=upline_id,password=random_num,adhaar_card=adhaar_card,pan_card=pan_card)
    data.save()
    return Response({"status": True, "message": "data created successfully"})
  # except:
    return Response({"status": False, "message": "not found"})
      


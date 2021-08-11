from django.shortcuts import render
# import africastalking
from .models import*
from .serializers import*
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def welcome(request):
    return render(request,'tekana.html') 
def about(request):
    return render(request,'about.html')
def program(request):
    return render(request,'program.html')
def donate(request):
    return render(request,'donate.html') 


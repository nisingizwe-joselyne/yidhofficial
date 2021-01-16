from django.shortcuts import render
import africastalking
from .models import*
from .serializers import*
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def welcome(request):
    return render(request,'smart.html') 
def about(request):
    return render(request,'about.html')


def registerEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = Farmers.objects.all()
        serializer = FarmerSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) #request data
        serializer = FarmerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'sucecesful', 'data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

def CooperativeEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = Cooperatives.objects.all()
        serializer = CoopeSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) #request data
        serializer = CoopeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'sucecesful', 'data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)    

def RecordEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = Record.objects.all()
        serializer = RecordSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) #request data
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'sucecesful', 'data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)        


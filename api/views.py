from django.shortcuts import render
from django.http import JsonResponse
from .serializers import ContactSerializer 
from rest_framework.decorators import api_view
from .models import Contact
from rest_framework import generics


@api_view(["POST","GET"])
def crate_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'msg': 'Message Send Success'})
    else:
        return JsonResponse({'msg': 'Message Error'})
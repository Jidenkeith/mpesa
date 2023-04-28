from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def auth_token(request):
    return HttpResponse("My mpesa")
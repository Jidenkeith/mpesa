from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.auth_token)
]


https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials

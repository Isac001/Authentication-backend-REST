# Django Imports
from django.urls import path  
from .views import *  

# Defining URL patterns for authentication-related views
urlpatterns = [
    # Endpoint for obtaining authentication tokens
    path("token/", CustomTokenObtainView.as_view(), name="token"),
]

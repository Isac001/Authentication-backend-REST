from django.urls import path
from .views import *  

urlpatterns = [
    path("token/", CustomTokenObtainView.as_view(), name="toke"),
]

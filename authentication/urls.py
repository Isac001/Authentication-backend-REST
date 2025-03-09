# Django Imports
from django.urls import path  
from .views import *  

# Defining URL patterns for authentication-related views
urlpatterns = [
    
    # Endpoint for obtaining authentication tokens
    path("", UserListView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete")
]

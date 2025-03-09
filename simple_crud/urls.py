# Importing necessary Django module for URL configuration
from django.urls import path

# Importing all views from the current module
from .views import *

# Defining URL patterns for the CRUD operations
urlpatterns = [
    # Route for listing all objects (GET request)
    path("", SimpleCRUDListView.as_view(), name="simple-crud-list"),

    # Route for retrieving a single object by its primary key (GET request)
    path("<int:pk>/", SimpleCRUDDetailView.as_view(), name="simple-crud-detail"),

    # Route for creating a new object (POST request)
    path("create/", SimpleCRUDCreateView.as_view(), name="simple-crud-create"),

    # Route for updating an existing object (PUT request)
    path("update/<int:pk>/", SimpleCRUDUpdateView.as_view(), name="simple-crud-update"),

    # Route for deleting an object (DELETE request)
    path("delete/<int:pk>/", SimpleCRUDDeleteView.as_view(), name="simple-crud-delete")
]

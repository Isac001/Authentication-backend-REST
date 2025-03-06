# Importing Django REST framework's serializer module
from rest_framework import serializers

# Importing the SimpleCRUD model
from .models import SimpleCRUD

# Defining a serializer for the SimpleCRUD model
class SimpleCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        # Specifying the model to be serialized
        model = SimpleCRUD

        # Including all fields from the model in the serializer
        fields = "__all__"

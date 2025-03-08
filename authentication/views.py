# Django Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Project Imports
from .serializers import CustomTokenObtainSerializer

# API view for handling user authentication and token generation
class CustomTokenObtainView(APIView):


    # Handles POST requests for user authentication
    def post(self, request):
        
        # Deserialize and validate the incoming authentication data
        serializer = CustomTokenObtainSerializer(data=request.data)

        # If authentication data is valid, return the generated tokens
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        # If authentication fails, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

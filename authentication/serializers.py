# Django Imports
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.db.models import Q

# Serializer for user model
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "user_name",
            "user_email",
            "password",
            "user_cpf"
        ]

# Serializer for handling user authentication and token generation
class CustomTokenObtainSerializer(serializers.Serializer):
    
    # Fields for user authentication
    user_email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    # Method to authenticate the user
    def authenticate_user(self, attrs):
        email = attrs.get("user_email")
        password = attrs.get("password")

        # Get the user model dynamically
        User = get_user_model()

        # Retrieve user by email
        user = User.objects.filter(Q(user_email=email)).first()

        # Check if user exists and the password is correct
        if user and user.check_password(password):
            return True, user

        return False, None

    # Method to generate and return JWT tokens
    def get_token_data(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    
    # Method to validate the provided credentials
    def validate(self, attrs):
        status, user = self.authenticate_user(attrs)

        # If authentication fails due to incorrect input format
        if not status:
            raise serializers.ValidationError("Please provide your credentials correctly!")

        # If authentication fails due to incorrect email or password
        if not user:
            raise serializers.ValidationError("Incorrect email and password combination!")

        # Return generated tokens upon successful authentication
        return self.get_token_data(user)

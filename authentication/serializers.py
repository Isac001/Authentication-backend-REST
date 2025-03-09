# Django Imports
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.db.models import Q

# Serializer for retrieving user details
class UserDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "user_name",
            "user_email",
            "password",
            "user_cpf"
        ]

# Serializer for creating a new user
class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "user_name",
            "user_email",
            "password",
            "user_cpf"
        ]
        
    # Method to create a new user, ensuring the password is properly set
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User.objects.create_user(**validated_data, password=password)
        return user

# Serializer for updating user information
class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "user_name"
        ]

    # Method to update the user name while keeping other fields unchanged
    def update(self, instance, validated_data):
        instance.user_name = validated_data.get("user_name", instance.user_name)
        instance.save()
        return instance

# Serializer for handling user authentication and token generation
class CustomTokenObtainSerializer(serializers.Serializer):
    
    user_email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    # Method to authenticate the user using email and password
    def authenticate_user(self, attrs):
        email = attrs.get("user_email")
        password = attrs.get("password")

        User = get_user_model()
        user = User.objects.filter(Q(user_email=email)).first()

        if user and user.check_password(password):
            return True, user

        return False, None

    # Method to generate refresh and access tokens for authenticated users
    def get_token_data(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    
    # Method to validate user credentials and return JWT tokens
    def validate(self, attrs):
        status, user = self.authenticate_user(attrs)

        if not status:
            raise serializers.ValidationError("Please provide your credentials correctly!")

        if not user:
            raise serializers.ValidationError("Incorrect email and password combination!")

        return self.get_token_data(user)

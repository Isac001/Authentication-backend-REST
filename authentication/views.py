# Django Imports
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# Project Imports
from .models import User
from .serializers import *


# Class responsible for handling user authentication and token generation.
class CustomTokenObtainView(APIView):

    # Receives user credentials and returns an access and refresh token if valid.
    def post(self, request):
        serializer = CustomTokenObtainSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class responsible for handling refresh token requests.
class CustomTokenRefreshView(TokenRefreshView):
    """
    Receives a valid refresh token and returns a new access token.
    """
    pass


# Class responsible for listing all registered users.
class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # Fetches all users and returns them as a serialized response.
    def get(self, request):
        users = self.get_queryset()
        serializers = self.serializer_class(users, many=True)
        return response.Response(serializers.data, status=status.HTTP_200_OK)


# Class responsible for retrieving user details by ID.
class UserDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # Fetches user details by ID and returns them as a serialized response.
    def get(self, request, pk):
        try:
            serializer = self.serializer_class(self.queryset.get(pk=pk))
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return response.Response({"error": "The user does not exist"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class responsible for creating new users.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # Receives user data, validates, and creates a new user.
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return response.Response(
                {"ERROR": "User already registered with this email or CPF"},
                status=status.HTTP_400_BAD_REQUEST
            )

        except ValidationError as e:
            return response.Response(
                {"ERROR": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return response.Response(
                {"ERROR": f"Internal server error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# Class responsible for updating user information.
class UserUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    # Receives user data and updates the corresponding user by ID.
    def put(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            serializer = self.serializer_class(user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return response.Response(
                {"ERROR": "Database integrity error"},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return response.Response(
                {"ERROR": f"Internal server error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# Class responsible for deleting a user.
class UserDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # Deletes a user by ID if they exist in the database.
    def delete(self, request, pk):
        try:
            obj = self.queryset.get(pk=pk)
            obj.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return response.Response({"error": "The user does not exist"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return response.Response({"error": "An error occurred while deleting"}, status=status.HTTP_400_BAD_REQUEST)

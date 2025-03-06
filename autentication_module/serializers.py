from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q


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



class CustomTokenObtainSerializer(serializers.Serializer):
    user_email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """
        Valida as credenciais do usuário e retorna os tokens de acesso.
        """
        # Autentica o usuário
        status, user = self.authenticate_user(attrs)

        if not status:
            raise serializers.ValidationError("Por favor, informe suas credenciais corretamente!")

        if not user:
            raise serializers.ValidationError("Combinação incorreta de e-mail e senha!")

        return self.get_token_data(user)

    def authenticate_user(self, attrs):
        """
        Método para autenticar o usuário pelo email e senha.
        """
        email = attrs.get("user_email")
        password = attrs.get("password")

        User = get_user_model()

        # Busca o usuário pelo e-mail
        user = User.objects.filter(Q(user_email=email)).first()

        # Verifica se a senha está correta
        if user and user.check_password(password):
            return True, user

        return False, None

    def get_token_data(self, user):
        """
        Gera os tokens JWT para o usuário autenticado.
        """
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainSerializer
import logging

# Configurando logging para depuração
logger = logging.getLogger(__name__)

class CustomTokenObtainView(APIView):

    def post(self, request):
        logger.info("Recebendo requisição de login...")
        logger.info(f"Dados recebidos: {request.data}")

        serializer = CustomTokenObtainSerializer(data=request.data)

        if serializer.is_valid():
            logger.info("Autenticação bem-sucedida!")
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        logger.warning(f"Falha na autenticação: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

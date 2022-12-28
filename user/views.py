from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from user.serializer import RegisterSerializer, LoginSerializer, TokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from _base.serializers.status_serializers import StatusSerializer
from _base.authentication import BearerAuthentication

class LoginView(CreateAPIView):
    """
    Login to the exists user.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=request.data.get(
            "username"), password=request.data.get("password"))
        if not user:
            serializer = StatusSerializer(data={'message': "Bad Credential"})
            serializer.is_valid(raise_exception=True)
            return Response(data=serializer.data, status=HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        data = {'token': token.key}
        serializer = TokenSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CreateUserView(CreateAPIView):
    
    permission_classes = [permissions.AllowAny]
    
    """
    Register as new user.
    """
    model = get_user_model()
    serializer_class = RegisterSerializer


class LogoutView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuthentication]

    def get(self, request):
        request.user.auth_token.delete()
        serializer = StatusSerializer(data={'message': "Logout"})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

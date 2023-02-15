from rest_framework import generics
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from .models import User


class Registration(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer



from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, AnonimousRegisterSerializer
from .models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class AnonymousRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AnonimousRegisterSerializer
    permission_classes = [permissions.AllowAny]

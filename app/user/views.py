from rest_framework import generics

from . import serializers

class CreateUserView(generics.CreateAPIView):
    """Creates a new user in the system"""
    serializer_class = serializers.UserSerializer

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializer import userserializer , groupserializer
from rest_framework import permissions , viewsets

# Create your views here.

class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer
    permission_classes = [permissions.IsAuthenticated]

class groupviewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupserializer
    permission_classes = [permissions.IsAuthenticated]


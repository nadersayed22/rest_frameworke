from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import USerProfile


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = USerProfile.objects.all()

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import filters
# Create your views here.
from rest_framework import generics

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'created_at']

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'created_at']
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import filters
# Create your views here.
from rest_framework import generics
from rest_framework import permissions



class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'created_at']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'created_at']


    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    


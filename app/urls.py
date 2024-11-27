
from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserView.as_view(), name = "User"),
    path('user/<int:pk>/', UserDetailView.as_view(), name = "User_detail"),
]

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import UserSerializers
from .models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializers
    permissions_classes = (AllowAny, )
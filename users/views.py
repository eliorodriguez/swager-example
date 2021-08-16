from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.generics import ListCreateAPIView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
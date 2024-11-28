from django.shortcuts import render
from rest_framework.response import Response

from .models import *
from rest_framework import generics, status
from .serializers import *
from rest_framework.permissions import AllowAny

class userCreateView(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = userSerializers
    permission_classes = [AllowAny]

class userDetailView(generics.RetrieveAPIView):
    queryset = users.objects.all()
    serializer_class = userSerializers

class userUpdateView(generics.RetrieveUpdateAPIView):
    queryset = users.objects.all()
    serializer_class = userSerializers

class userDeleteView(generics.DestroyAPIView):
    queryset = users.objects.all()
    serializer_class = userSerializers


class adminCreateView(generics.ListCreateAPIView):
    queryset = admin.objects.all()
    serializer_class = adminSerializers

class adminDetails(generics.RetrieveAPIView):
    queryset = admin.objects.all()
    serializer_class = adminSerializers

class adminUpdateView(generics.RetrieveUpdateAPIView):
    queryset = admin.objects.all()
    serializer_class = adminSerializers



class adminDelete(generics.DestroyAPIView):
    queryset = admin.objects.all()
    serializer_class = adminSerializers


class bookcreateview(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializers
    permission_classes = [AllowAny]

class bookdetailview(generics.RetrieveAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializers

class bookupdateview(generics.RetrieveUpdateAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializers



class bookdeleteview(generics.DestroyAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializers


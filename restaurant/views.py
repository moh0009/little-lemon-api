from django.shortcuts import render
from . import models
from rest_framework import generics
from . import serializers
# Create your views here.
#Menu views
class MenuAll(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class MenuSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
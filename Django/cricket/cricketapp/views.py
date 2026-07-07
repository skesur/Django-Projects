from django.shortcuts import render
from rest_framework import viewsets
from .models import Cricket
from .serializers import CricketSerializer

# Create your views here.
class CricketViewset(viewsets.ModelViewSet):
    queryset=Cricket.objects.all()
    serializer_class=CricketSerializer
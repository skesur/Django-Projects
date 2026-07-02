from django.shortcuts import render
from .serializers import EmployeeSerializers,CompanySerializers
from rest_framework import viewsets
from .models import Company,Employee

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
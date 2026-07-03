from django.shortcuts import render
from .serializers import EmployeeSerializers,CompanySerializers
from rest_framework import viewsets
from .models import Company,Employee
from .permission import isAdminorReadonly

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    permission_classes=[isAdminorReadonly]

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    permission_classes=[isAdminorReadonly]
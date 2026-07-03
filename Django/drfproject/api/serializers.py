from rest_framework import serializers
from .models import Company,Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class CompanySerializers(serializers.ModelSerializer):
    employees=EmployeeSerializers(many=True,read_only=True)
    class Meta:
        model=Company
        fields='__all__'
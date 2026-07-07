from rest_framework import serializers
from .models import Cricket

class CricketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cricket
        fields='__all__'
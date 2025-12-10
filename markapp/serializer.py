from rest_framework import serializers
from .models import marksheet

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = marksheet
        fields = '__all__'

from dataclasses import fields
from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
from .models import User, PrivateTaskModel
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], 
                                        password=validated_data['password'])
        
        validated_data['refresh'] = user.refresh
        validated_data['access'] = user.access
        
        return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    
        
    def validate(self,data):
        
        try: 
            User.objects.get(username=data['username'])
        except:
            raise ValidationError(
                {'msg':'User Doesn’t Exist'}
            )
        
        user = authenticate(username=data['username'],password=data['password'])

        if not user:
            raise ValidationError(
                {'msg':'Invalid Credentials'}
            )
        data['refresh'] = user.refresh
        data['access'] = user.access
        return data
        
    def create(self, validated_data):
        return validated_data

class PrivateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateTaskModel
        fields = '__all__'

class PrivateTaskTogle(serializers.Serializer):
    task_id = serializers.CharField(write_only=True)
    
    def update(self, instance, validated_data):
        task = PrivateTaskModel.objects.get(id=validated_data['task_id'])
        
        if task.is_completed == True:
            task.is_completed = False
        else:
            task.is_completed = True
        
        task.save()
        return validated_data
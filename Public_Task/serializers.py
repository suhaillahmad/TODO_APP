from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    

class PublicTaskTogle(serializers.Serializer):
    task_id = serializers.CharField(write_only=True)
    
    def update(self, instance, validated_data):
        task = Task.objects.get(id=validated_data['task_id'])
        
        if task.is_completed == True:
            task.is_completed = False
        else:
            task.is_completed = True
        
        task.save()
        return validated_data
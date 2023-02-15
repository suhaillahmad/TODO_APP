from rest_framework import generics
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class TaskView(generics.CreateAPIView,
           generics.ListAPIView,
           generics.DestroyAPIView,
           generics.UpdateAPIView):
    
    serializer_class = TaskSerializer
    
    # Returns an object instance
    
    def get_object(self):
        return Task.objects.get(id=self.request.data.get('task_id'))
    
    # Get API for getting Completed and Not Completed Task
    
    def get_queryset(self):
        return Task.objects.filter(is_completed=str(self.request.GET.get('completed')).capitalize()).order_by('-time')
    
    # Post API For Creating Task
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    # Patch API For Updating Task
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    # Delete API For Deteleting a Task

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
        
    
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import PublicTaskTogle, TaskSerializer
from .models import Task


class TaskView(generics.CreateAPIView,
           generics.ListAPIView,
           generics.DestroyAPIView,
           generics.UpdateAPIView):
    
    serializer_class = TaskSerializer
    
    # Returns an object instance
    
    def get_object(self):
        return Task.objects.get(id=self.request.GET.get('task_id'))
    
    # Get API for getting Completed and Not Completed Task
    
    def get_queryset(self):
        return Task.objects.all().order_by('-time')
    
    # Post API For Creating Task
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    # Patch API For Updating Task
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    # Delete API For Deteleting a Task

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
        



class ToggleForUpdateStatusForTaskPublic(generics.UpdateAPIView):
    serializer_class = PublicTaskTogle
    
    # Returns an object instance
    
    def get_object(self):
        return Task.objects.get(id=self.request.GET.get('task_id'))
    
    # Api to mark the task as complete / Incomplete
    
    def patch(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({'message':'Task Status Updated Successfully'}, status=status.HTTP_200_OK)
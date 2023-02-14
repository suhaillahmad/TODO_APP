from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import *
from .models import *


class TaskView(generics.CreateAPIView,
           generics.ListAPIView,
           generics.DestroyAPIView,
           generics.UpdateAPIView):
    
    serializer_class = TaskSerializer
    
    def get_object(self):
        return Task.objects.get(id=self.request.data.get('task_id'))
    def get_queryset(self):
        return Task.objects.all().order_by('-time')
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
        
    
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import LoginSerializer, PrivateTaskSerializer, PrivateTaskTogle, RegisterSerializer
from .models import PrivateTaskModel
from rest_framework.permissions import IsAuthenticated


class Registration(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
class PrivateTaskView(generics.CreateAPIView,
                      generics.ListAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView):
    serializer_class = PrivateTaskSerializer
    permission_classes = [IsAuthenticated,]
    
    # Returns an object instance
    
    def get_object(self):
        return PrivateTaskModel.objects.get(id=self.request.data.get('task_id'))
    
    # Get API for getting Completed and Not Completed Task
    
    def get_queryset(self):
        return PrivateTaskModel.objects.filter(user=self.request.user.id).order_by('-time')
    
    # Post API For Creating Task
    
    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)
    
    # Patch API For Updating Task
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    # Delete API For Deteleting a Task

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Api to mark the task as complete / Incomplete

class ToggleForUpdateStatusForTask(generics.UpdateAPIView):
    serializer_class = PrivateTaskTogle
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return PrivateTaskModel.objects.get(id=self.request.data.get('task_id'))
    
    def patch(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({'message':'Task Status Updated Successfully'}, status=status.HTTP_200_OK)


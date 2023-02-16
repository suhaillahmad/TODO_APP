from django.urls import path
from .views import Registration,LoginView,PrivateTaskView,ToggleForUpdateStatusForTask

urlpatterns = [
    path('Register/', Registration.as_view()),
    path('login/', LoginView.as_view()),
    path('task/', PrivateTaskView.as_view()),
    path('task_status_update/', ToggleForUpdateStatusForTask.as_view())
]

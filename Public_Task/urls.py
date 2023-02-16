from django.urls import path
from .views import TaskView, ToggleForUpdateStatusForTaskPublic

urlpatterns = [
        path('task/', TaskView.as_view()),
        path('task_status_update/', ToggleForUpdateStatusForTaskPublic.as_view())
]

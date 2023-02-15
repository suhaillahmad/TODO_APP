from django.urls import path
from .views import *

urlpatterns = [
    path('Register/', Registration.as_view()),
    path('login/', LoginView.as_view())
]

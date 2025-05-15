from django.urls import path
from . import views
from .views import TaskListCreateAPIView
from .views import TaskDetailAPIView

urlpatterns = [
    path('api/', TaskListCreateAPIView.as_view(), name='task_list_api'),
    path('api/<int:pk>/', TaskDetailAPIView.as_view(), name= 'task_api_detail'),
]   
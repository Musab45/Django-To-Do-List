from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'completed', 'created_at', 'owner'] # or user '__all__' to use all fields
        read_only_fields = ['owner', 'created_at']

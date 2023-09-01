from rest_framework import serializers

from apps.todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        
        fields = ["id", "name", "description", "date", "user"] # dados do models.py
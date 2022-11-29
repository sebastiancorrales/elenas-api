# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# Model
from apps.tasks.models import Tasks


class TasksModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tasks
        exclude = ['updated_at', 'created_at']


class TasksSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)
    type_task_id = serializers.CharField(max_length=20, required=False)

    def create(self, data):
        task = Tasks.objects.create(**data)
        return task

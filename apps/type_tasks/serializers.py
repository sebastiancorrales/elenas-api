# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# Model
from apps.type_tasks.models import TypeTasks


class TypeTasksModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = TypeTasks
        exclude = ['updated_at', 'created_at']


class TypeTasksSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255,  validators=[UniqueValidator(queryset=TypeTasks.objects.all())])
    description = serializers.CharField(max_length=1000)

    def create(self, data):

        type_task = TypeTasks.objects.create(**data)
        return type_task

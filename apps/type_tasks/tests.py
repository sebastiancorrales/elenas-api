# Django
from django.test import TestCase
import json
from rest_framework.test import APIClient
from rest_framework import status

# Models
from apps.type_tasks.models import TypeTasks


class TypeTasksTest(TestCase):
    def setUp(self):
        type_task = TypeTasks.objects.create(
            name='sebastiancorrales477@gmail.com',
            description='Testing',
            completed=False
        )
        

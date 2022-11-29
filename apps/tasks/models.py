import json
# Django
from django.db import models
from apps.users.models import User
from apps.type_tasks.models import TypeTasks

class Tasks(models.Model):

    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type_task = models.ForeignKey(TypeTasks, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Tasks'

    def __str__(self):
        data = {
            'id': self.id,
            'name': self.name
        }
        return json.dumps(data)

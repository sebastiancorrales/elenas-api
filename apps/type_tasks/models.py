import json
# Django
from django.db import models

class TypeTasks(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'type_tasks'
        verbose_name = 'type_tasks'

    def __str__(self):
        data = {
            'id': self.id,
            'name': self.name
        }
        return json.dumps(data)

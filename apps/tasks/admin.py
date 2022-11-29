from django.contrib import admin

# Register your models here.
from apps.tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

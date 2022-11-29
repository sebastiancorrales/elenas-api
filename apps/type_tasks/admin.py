from django.contrib import admin

# Register your models here.
from apps.type_tasks.models import TypeTasks


@admin.register(TypeTasks)
class TypeTasksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.tasks import views


router = DefaultRouter()
router.register('tasks', views.TasksViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('update-task/', views.UpdateTaskViewSet.as_view()),
    path('delete-task/', views.DeleteTaskViewSet.as_view())
]

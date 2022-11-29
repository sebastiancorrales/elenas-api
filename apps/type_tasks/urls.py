# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.type_tasks import views


router = DefaultRouter()
router.register('type-tasks', views.TypeTasksViewSet, basename='type-tasks')

urlpatterns = [
    path('', include(router.urls))
]

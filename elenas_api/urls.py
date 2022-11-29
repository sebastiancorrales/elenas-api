from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.db.models import Max, Min, Sum, Q

base_url = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(base_url, include(('apps.tasks.urls', 'tasks'), namespace='tasks')),
    path(base_url, include(('apps.type_tasks.urls', 'tasks'), namespace='type-tasks')),
    path(base_url, include(('apps.users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
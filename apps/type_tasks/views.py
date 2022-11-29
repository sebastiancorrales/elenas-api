# Django REST Framework
from rest_framework import viewsets
# Models
from apps.type_tasks.models import TypeTasks
from apps.type_tasks.serializers import TypeTasksModelSerializer
# Permissions
from apps.users.permissions import ActualDjangoModelPermissions


class TypeTasksViewSet(viewsets.ModelViewSet):

    queryset = TypeTasks.objects.all()
    serializer_class = TypeTasksModelSerializer

    def get_permissions(self):
        permission_classes = [ActualDjangoModelPermissions]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        try:
            data = {}
            for request in self.request.query_params:
                if self.request.query_params.get(request) is not None:
                    data[request] = self.request.query_params.get(request)

            queryset = TypeTasks.objects.filter(**data)

            return queryset
        except Exception as e:
            exception = {
                'status': "failed",
                'message': e.args
            }

            return exception

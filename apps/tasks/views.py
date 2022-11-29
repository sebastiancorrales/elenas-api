# Django REST Framework
from rest_framework import viewsets, status
# Models
from apps.tasks.models import Tasks
from apps.tasks.serializers import TasksModelSerializer
# Permissions
from apps.users.permissions import ActualDjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime


class TasksViewSet(viewsets.ModelViewSet):

    queryset = Tasks.objects.all()
    serializer_class = TasksModelSerializer

    def get_permissions(self):
        permission_classes = [ActualDjangoModelPermissions]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        try:
            data = {"user_id": self.request.user.id}
            for request in self.request.query_params:
                if self.request.query_params.get(request) is not None:
                    if 'description' == request:
                        data['description__contains'] = self.request.query_params.get(request)
                    else:
                        data[request] = self.request.query_params.get(request)
            print(data)
            queryset = Tasks.objects.filter(**data)

            return queryset
        except Exception as e:
            exception = {
                'status': "failed",
                'message': e.args,
                'msg': e.args
            }

            return exception

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateTaskViewSet(APIView):
    def put(self, request):
        try:
            pk = request.data.get('id', 0)
            user = request.user
            Tasks.objects.filter(user_id=user.id, pk=pk).update(**request.data)
            task = object_to_dict(Tasks.objects.get(user_id=user.id, pk=pk))
            return Response(task, status=status.HTTP_200_OK)
        except Exception as e:
            exception = {
                "message":e.args
            }
            return Response(exception, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteTaskViewSet(APIView):
    def delete(self, request):
        try:
            pk = request.data.get('id', 0)
            user = request.user
            Tasks.objects.get(user_id=user.id, pk=pk).delete()
            return Response({"message": "Tarea eliminada correctamente"}, status=status.HTTP_200_OK)
        except Exception as e:
            exception = {
                "message":e.args
            }
            return Response(exception, status=status.HTTP_400_BAD_REQUEST)

def object_to_dict(object):
    '''This function converts a model object into a dictionary.
    
    :param object: The model object.
    :return: A dictionary of the model object.
    '''
    _object = object.__dict__
    if 'created_at' in _object:
        _object['created_at'] = str(datetime.strftime(_object['created_at'], "%Y-%m-%d"))
        
    if 'updated_at' in _object:
        _object['updated_at'] = str(datetime.strftime(_object['updated_at'], "%Y-%m-%d"))

    result = {}
    for i in _object:
        if i != '_state':
            result[i] = _object[i]
    return result
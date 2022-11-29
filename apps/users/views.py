# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from apps.users.permissions import ActualDjangoModelPermissions
from apps.users.serializers import UserModelSerializer, UserSignUpSerializer
from apps.users.models import User

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    def get_permissions(self):
        permission_classes = [ActualDjangoModelPermissions]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        try:
            data = {}
            for request in self.request.query_params:
                if self.request.query_params.get(request) is not None:
                    data[request] = self.request.query_params.get(request)

            queryset = User.objects.filter(**data)

            return queryset
        except Exception as e:
            exception = {
                'status': "failed",
                'message': e.args
            }
            return exception

    @action(detail=False, methods=['post'])
    def signup(self, request):

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)


class Login(TokenObtainPairView):

    def post(self, request):

        username = request.data.get('username', '')
        password = request.data.get('password', '')
        print(username)
        print(password)
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserModelSerializer(user)

                return Response({
                    'access_token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)

            return Response({'error': 'No se pudo iniciar sesion'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Nombre de Usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class BlackListTokenUpdateView(APIView):

    queryset = User.objects.none()

    def get_permissions(self):
        permission_classes = [ActualDjangoModelPermissions]
        return [permission() for permission in permission_classes]

    def post(self, request):

        try:
            refresh_token = request.data["refresh-token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'Sesion Cerrada Correctamente'}, status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            exception = {'message': e.args}
            return Response(exception, status=status.HTTP_400_BAD_REQUEST)

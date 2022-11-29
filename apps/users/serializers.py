# Django
from django.contrib.auth import password_validation, authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Models
from apps.users.models import User

class UserModelSerializer(serializers.ModelSerializer):
        
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
     )  
    
    class Meta:

        model = User
        fields = ['id', 'is_active', 'identification', 'first_name', 'last_name', 'email', 'username', 'groups']
        extra_kwargs = {'password':{'write_only':True}}

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSignUpSerializer(serializers.Serializer):
    
    identification = serializers.CharField(
        min_length=5, 
        max_length=100, 
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(min_length=1, max_length=100)
    last_name = serializers.CharField(min_length=1, max_length=100)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone = serializers.CharField(min_length=10, max_length=10)
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=5, max_length=64)
    password_confirmation = serializers.CharField(min_length=5, max_length=64)
    
    
    def validate(self, data):

        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(password)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user


class UserLoginSerializer(serializers.Serializer):
    
    identification = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
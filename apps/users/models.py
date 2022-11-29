import json
# Django
from django.db import models
import django.contrib.auth.validators
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import AbstractUser
# Models


class User(AbstractUser):

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    identification = models.BigIntegerField('identification', unique=True, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField('email address', unique=True)
    phone = models.BigIntegerField('phone', unique=True, null=True)
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    password = models.CharField(max_length=120)
    password_confirmation = models.CharField(max_length=120)
    groups = models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')
    user_permissions = models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')
    is_superuser = models.BooleanField(default=False,)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    date_joined = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    email_verified_at = models.DateTimeField(null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='users'
    
    def __str__(self):

        data = {
            'id': self.id, 
            'identification': self.identification, 
            'first_name': self.first_name, 
            'last_name': self.last_name
        }
        return json.dumps(data)
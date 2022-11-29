# Django
from django.test import TestCase
import json
from rest_framework.test import APIClient
from rest_framework import status

# Models
from apps.users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            email='sebastiancorrales477@gmail.com',
            first_name='Testing',
            last_name='Testing',
            username='sebastiancorrales477'
        )
        user.set_password('admin123')
        user.save()

    def test_signup_user(self):
        """Check if we can create an user"""
        client = APIClient()
        response = client.post(
                'api/v1/users/signup/', {
                'email': 'sebastiancorrales477@gmail.com',
                'password': 'rc{4@qHjR>!b`yAV',
                'password_confirmation': 'rc{4@qHjR>!b`yAV',
                'first_name': 'Testing',
                'last_name': 'Testing',
                'phone': '999888777',
                'username': 'testing1'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {"username":"testing1","first_name":"Testing","last_name":"Testing","email":"sebastiancorrales477@gmail.com"})

    
    def test_login_user(self):

        client = APIClient()
        response = client.post(
                'api/v1/users/login/', {
                'email': 'sebastiancorrales477@gmail.com',
                'password': 'admin123',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        result = json.loads(response.content)
        self.assertIn('access_token', result)
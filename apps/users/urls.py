# Django
from django.urls import include, path
# Django REST Framework
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from apps.users.views import BlackListTokenUpdateView, Login
# Views
from apps.users import views as user_views

router = DefaultRouter()
router.register('users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='login'),
    path('logout/', BlackListTokenUpdateView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

from django.contrib import admin
from django.urls import path, include

from .views import AuthAPIView, RegisterAPIView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
]

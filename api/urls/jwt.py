from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

jwt_urls = [
     path('login', TokenObtainPairView.as_view()),
     path('refresh-token', TokenRefreshView.as_view()),
]

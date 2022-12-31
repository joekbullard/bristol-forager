# accounts/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignUpView, CustomUserDetailAPI, CustomUserListAPI


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('api/users/', CustomUserListAPI.as_view()), # new
    path('api/users/<int:pk>/', CustomUserDetailAPI.as_view()), # new
]

urlpatterns = format_suffix_patterns(urlpatterns)
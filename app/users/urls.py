# accounts/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignUpView, CustomUserDetailAPI, CustomUserListAPI
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("api/users/", CustomUserListAPI.as_view()),  # new
    path("api/users/<int:pk>/", CustomUserDetailAPI.as_view()),  # new
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

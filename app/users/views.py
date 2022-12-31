# accounts/views.py
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomUserListAPI(generics.ListAPIView): # new
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailAPI(generics.RetrieveAPIView): # new
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
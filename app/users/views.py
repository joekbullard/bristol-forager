# accounts/views.py
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # super() gives access to parent class and creates object representation
        valid = super(SignUpView, self).form_valid(form)
        # get cleaned data from form (email and password)
        email, password = form.cleaned_data.get("email"), form.cleaned_data.get(
            "password1"
        )
        # authenticate new user
        new_user = authenticate(email=email, password=password)
        # login user
        login(self.request, new_user)
        return valid


class CustomUserListAPI(generics.ListAPIView):  # new
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailAPI(generics.RetrieveAPIView):  # new
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

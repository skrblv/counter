from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm # Больше не нужна напрямую
from .forms import CustomUserCreationForm, CustomAuthenticationForm # Импортируем обе наши формы

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm # <-- Указываем нашу кастомную форму входа

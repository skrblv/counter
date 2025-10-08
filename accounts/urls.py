from django.urls import path
from .views import SignUpView, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('signup/', SignUpView.as_view(), name='register'),
        path('login/', CustomLoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    ]

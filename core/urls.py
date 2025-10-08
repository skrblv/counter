from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('increment/', views.increment_count, name='increment_count'),
        path('decrement/', views.decrement_count, name='decrement_count'),
        path('statistics/', views.statistics, name='statistics'),
    ]

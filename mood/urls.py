from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log_mood, name='log_mood'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
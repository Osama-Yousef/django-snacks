from .views import HomeView, AboutView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'), ## Adding home url using HomeView
    path('about', AboutView.as_view(), name='about'),
]
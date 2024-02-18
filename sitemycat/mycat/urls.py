from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('video/', views.video, name='video'),
    path('photo/', views.photo, name='photo'),
]
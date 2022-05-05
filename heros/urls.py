
from django.urls import path
from . import views

urlpatterns = [
    path('hero/', views.view_hero_user, name='view_hero_user'),
]

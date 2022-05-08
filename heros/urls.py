
from django.urls import path
from . import views

urlpatterns = [
    path('hero/', views.view_hero_user, name='view_hero_user'),
    path('hero/edit-hero/<int:specifications_id>/', views.edit_hero,
         name='edit_hero')
]

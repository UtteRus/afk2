from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('hero/', views.view_hero_user, name='view_hero_user'),
    path('hero/edit-hero/<int:specifications_id>/', views.edit_hero,
         name='edit_hero')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

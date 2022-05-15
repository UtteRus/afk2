from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('hero/', views.ViewHeroUserAPIList.as_view(), name='view_hero_user'),
    path('hero/edit-hero/<int:specifications_pk>/',
         views.EditHeroAPI.as_view(), name='edit_hero'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('registration/', views.RegistrationAPI.as_view(),
         name='registration'),
]

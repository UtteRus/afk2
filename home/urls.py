from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('registration/', views.RegistrationAPI.as_view(), name='registration')
    ,
]

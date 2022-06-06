from django.forms import model_to_dict
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from heros.models import Specifications, Hero
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from home.serializers import RegistrationSerializers, ProfileSerializers, \
    LoginSerializers
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout


class RegistrationAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/registration.html'

    def get(self, request):
        serializer = RegistrationSerializers
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = RegistrationSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, })
        serializer.save()
        return redirect('home_page')


class LoginAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/login.html'

    def get(self, request):
        serializer = LoginSerializers
        return Response({'serializer': serializer})

    def post(self, request):
        pass


def home_page(request):
    return render(request, 'home/home.html')


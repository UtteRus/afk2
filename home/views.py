from django.forms import model_to_dict
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from heros.models import Specifications, Hero
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from home.serializers import RegistrationSerializers, ProfileSerializers
from .models import Profile
from rest_framework.permissions import IsAuthenticated


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


def login(request):
    return render(request, 'home/login.html')


def home_page(request):
    return render(request, 'home/home.html')


def registration(request):
    return render(request, 'home/registration.html')

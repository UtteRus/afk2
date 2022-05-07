from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'home/login.html')


def home_page(request):
    return render(request, 'home/home.html')


def registration(request):
    pass
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def view_hero_user(request):
    return render(request, 'hero/view_hero_user.html')

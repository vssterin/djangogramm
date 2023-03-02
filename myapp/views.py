from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Photo


def index(request):
    phtot = Photo.objects.all()[0]
    print(phtot.image_thumbnail.url)
    return HttpResponse('Страница')


def posts(request):
    return HttpResponse('Лента')


def profile(request):
    return HttpResponse('Профиль')

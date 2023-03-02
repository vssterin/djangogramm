from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Photo, Post, UserProfile


def index(request):
    return HttpResponse('Страница')


def posts(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.tags.count())
    return render(request, 'posts.html', {'posts': Post.objects.all(),
                                          'images': Photo.objects.all(),
                                          'user_data': UserProfile.objects.all()})


def profile(request):
    return HttpResponse('Профиль')

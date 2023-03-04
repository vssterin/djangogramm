from django.contrib.auth.models import User, AbstractUser
from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Photo, Post, UserProfile, Tag


def index(request):
    return HttpResponse('Страница')


def posts(request):
    return render(request, 'posts.html', {'posts': Post.objects.all(),
                                          'images': Photo.objects.all(),
                                          'user_data': UserProfile.objects.all()})


def profile(request, profile_id):
    posts = Post.objects.filter(user_id=profile_id)
    context = {
        'posts': posts,
        'title': posts[0].user.username,
        'name': f'{posts[0].user.first_name} {posts[0].user.last_name}'
    }
    return render(request, 'profile.html', context=context)

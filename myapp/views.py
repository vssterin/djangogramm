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
    user = User.objects.get(id=profile_id)
    posts = user.posts.all()
    context = {
        'posts': posts,
        'title': user.username,
        'name': f'{user.first_name} {user.last_name}',
        'images': Photo.objects.all()
    }
    return render(request, 'profile.html', context=context)

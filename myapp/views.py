from itertools import chain
from django.views.generic import ListView
from django.contrib.auth.models import User, AbstractUser
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from myapp.models import Photo, Post, UserProfile, Tag, Like


def follow_unfollow_profile(request):
    if request.method == 'POST':
        my_profile = UserProfile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = UserProfile.objects.get(pk=pk)
        if obj.user in my_profile.fallowing.all():
            my_profile.fallowing.remove(obj.user)
        else:
            my_profile.fallowing.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile')


def index(request):
    context = {
        'title': 'Main Page',
    }
    return render(request, 'index.html', context=context)
    # return HttpResponse('Страница')


def posts(request):
    context = {'posts': Post.objects.all(),
               'images': Photo.objects.all(),
               'user_data': UserProfile.objects.all(),
               'main_user': request.user,
               }
    return render(request, 'posts.html', context=context)


def like_post(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)

            if user in post_obj.likes.all():
                post_obj.likes.remove(user)
            else:
                post_obj.likes.add(user)

            like, created = Like.objects.get_or_create(user=user, post_id=post_id)

            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                else:
                    like.value = 'Like'
            like.save()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('You must log in to like posts')

def profile(request, profile_id):
    posts = Post.objects.filter(owner__user__id=profile_id)
    view_profile = UserProfile.objects.get(user__id=profile_id)
    my_profile = UserProfile.objects.get(user__id=request.user.id)
    if view_profile.user in my_profile.fallowing.all():
        follow = True
    else:
        follow = False
    context = {
        'posts': posts,
        'title': view_profile.user.username,
        'name': f'{view_profile.user.first_name} {view_profile.user.last_name}',
        'follow': follow,
        'view_profile': view_profile,
    }
    return render(request, 'profile.html', context=context)


def news_feed(request):
    main_user = request.user
    user_profile = main_user.profile
    posts = Post.objects.filter(Q(owner=user_profile) | Q(owner__user__in=UserProfile.objects.get(user=main_user).fallowing.all())).order_by('-created_at')
    if posts:
        return render(request, 'news_feed.html', context={'posts': posts, 'main_user': main_user,})
    else:
        return HttpResponse('Нет постов')


def users(request):
    all_profiles = User.objects.all().exclude(id=request.user.id)
    profile = UserProfile.objects.get(user=request.user)
    context = {
        'profiles': all_profiles,
        'my_user': profile,
    }
    return render(request, 'users.html', context=context)
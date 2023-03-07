from django.contrib.auth.models import User, AbstractUser
from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import Photo, Post, UserProfile, Tag, Like


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

        return redirect('posts')
    else:
        return HttpResponse('You must log in to like posts')

def profile(request, profile_id):
    posts = Post.objects.filter(user_id=profile_id)
    context = {
        'posts': posts,
        'title': posts[0].user.username,
        'name': f'{posts[0].user.first_name} {posts[0].user.last_name}'
    }
    return render(request, 'profile.html', context=context)

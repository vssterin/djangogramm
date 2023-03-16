from django.urls import path
from .views import *

urlpatterns = [
    path('', posts, name='posts'),
    path('profile/<int:profile_id>', profile, name='profile'),
    path('like/', like_post, name='like-post'),
    path('news/', news_feed, name='news'),
    path('profile/', users, name='users'),
    path('switch_follow/', follow_unfollow_profile, name='switch_follow'),
]
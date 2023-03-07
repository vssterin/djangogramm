from django.urls import path
from .views import *

urlpatterns = [
    path('', posts, name='posts'),
    path('profile/<int:profile_id>', profile, name='profile'),
    path('like/', like_post, name='like-post'),
]
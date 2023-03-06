from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/', posts, name='posts'),
    path('profile/<int:profile_id>', profile, name='profile'),
]
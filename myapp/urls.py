from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('post/', posts),
    path('profile/<int:profile_id>', profile, name='profile'),
]
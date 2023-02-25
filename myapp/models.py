from django.db import models
from django.contrib.auth.admin import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    nickname = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ImageField(upload_to='icons/%Y/%m/%d/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_use_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Tag(models.Model):
    name = models.CharField(max_length=120, null=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(UserProfile)
    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.pk


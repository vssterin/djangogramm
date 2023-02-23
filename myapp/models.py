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


class VisualContent():
    image = models.ImageField(upload_to='icons/% Y/% m/% d/')





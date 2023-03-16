from django.db import models
from django.contrib.auth.admin import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


class UserProfile(models.Model):
    nickname = models.CharField(max_length=100, null=True, blank=True)
    icon = ProcessedImageField(upload_to='icons/%Y/%m/',
                               processors=[ResizeToFill(50, 50)],
                               format='JPEG',
                               options={'quality': 60}, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fallowing = models.ManyToManyField(User, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def profile_posts(self):
        return self.posts.all()

    class Meta:
        ordering = ('-created_at',)

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
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

    @property
    def num_likes(self):
        return self.likes.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/', null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(480, 600)],
                                     format='JPEG',
                                     options={'quality': 60},
                                     )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)



from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from myapp.models import Post


class TestPageTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create(username='Miki', first_name='Mike', last_name='Devars')
        post_1 = Post.objects.create(title='First Post',
                                     content='Heroku automatically identifies your app as a Python app if any of the following files are present in its root directory',
                                     user=user_1)
        self.client = Client()

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'All posts')

    def test_index_page(self):
        url = reverse('posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_index_page(self):
        user = Post.objects.get(id=1)
        url = reverse('profile', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, ' <h3>Heroku automatically identifies your app as a Python app if any of the following files are present in its root directory</h3>')
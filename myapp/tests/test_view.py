from django.test import TestCase
from myapp.models import Post, User

class PostsTestCase(TestCase):
    def test_posts(self):
        user_1 = User.objects.create(username='Miki', first_name='Mike', last_name='Devars')
        post_1 = Post.objects.create(title='First Post',
                                     content='Heroku automatically identifies your app as a Python app if any of the following files are present in its root directory',
                                     user=user_1)
        self.assertEqual(user_1.username, 'Miki')
        self.assertEqual(user_1.first_name, 'Mike')
        self.assertEqual(user_1.last_name, 'Devars')
        self.assertEqual(post_1.title, 'First Post')
        self.assertEqual(post_1.content, 'Heroku automatically identifies your app as a Python app if any of the following files are present in its root directory')
        self.assertEqual(post_1.user.first_name, 'Mike')
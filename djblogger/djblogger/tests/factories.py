import factory
from django.contrib.auth.models import User

from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = 'testing123'
    username = 'testuser'
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'X'
    subtitle = 'X'
    slug = 'X'
    author = factory.SubFactory(UserFactory)
    content = 'xyz'
    status = 'published'

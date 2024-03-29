import factory
from django.contrib.auth.models import User

from djblogger.blog.models import Post

from decouple import config


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = config('USERNAME')
    password = config('PASSWORD')
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "X"
    subtitle = "X"
    slug = "X"
    author = factory.SubFactory(UserFactory)
    content = "xyz"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)

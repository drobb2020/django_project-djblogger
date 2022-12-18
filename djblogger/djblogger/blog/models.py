from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):

    options = (
        ("draft", "Draft"),
        ('review', "Review"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=options, default="draft")
    tags = TaggableManager()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
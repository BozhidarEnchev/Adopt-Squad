from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models


class PublishableContentBase(models.Model):
    content = models.TextField(
        max_length=1000,
    )

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )

    time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class Post(PublishableContentBase, models.Model):
    title = models.CharField(
        max_length=100,
    )

    image = CloudinaryField('image', blank=True, null=True, folder='adopt-squad/forum-post-pictures/',
                            format='png')

    def __str__(self):
        return self.title


class Comment(PublishableContentBase, models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    def __str__(self):
        return self.content

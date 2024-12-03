from cloudinary.models import CloudinaryField
from django.db import models
from AdoptSquad.forum.mixins import PublishableContentMixin


class Post(PublishableContentMixin, models.Model):
    title = models.CharField(
        max_length=100,
    )

    image = CloudinaryField('image', blank=True, null=True, folder='adopt-squad/forum-post-pictures/',
                            format='png')

    def __str__(self):
        return self.title


class Comment(PublishableContentMixin, models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    def __str__(self):
        return self.content

from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField(
        max_length=1000,
    )

    image = CloudinaryField('image', blank=True, null=True, folder='adopt-squad/forum-post-pictures/',
                            format='png')

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.title

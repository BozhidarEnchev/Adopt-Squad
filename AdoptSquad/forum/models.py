from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField(
        max_length=1000,
    )

    image = models.ImageField(
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )

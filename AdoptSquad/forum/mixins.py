from django.contrib.auth import get_user_model
from django.db import models


class PublishableContentMixin(models.Model):
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

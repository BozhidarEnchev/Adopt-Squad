from cloudinary.models import CloudinaryField
from django.db import models


class Photo(models.Model):
    photo = CloudinaryField(
        'photo',
        folder='adopt-squad/gallery-pictures',
        format='png',
    )

    time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = CloudinaryField('image', blank=True, null=True, folder='adopt-squad/profile-pictures/',
                                      format='png')

    def __str__(self):
        return self.username

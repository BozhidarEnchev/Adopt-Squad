from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='adopt-squad/profile-pictures/', blank=True, null=True)

    def __str__(self):
        return self.username

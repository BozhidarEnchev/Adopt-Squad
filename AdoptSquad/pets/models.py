from cloudinary.models import CloudinaryField
from django.db import models

from AdoptSquad.pets.choices import PersonalityChoices


class Pet(models.Model):
    name = models.CharField(
        max_length=50
    )

    years = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    months = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    pet_picture = CloudinaryField(
        'image',
        folder='adopt-squad/pet-pictures',
        format='png',
    )

    personality = models.CharField(
        max_length=50,
        choices=PersonalityChoices.choices,
    )

    def __str__(self):
        return self.name


class Dog(Pet):
    leash_trained = models.BooleanField()


class Cat(Pet):
    pass

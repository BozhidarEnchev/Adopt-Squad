from cloudinary.models import CloudinaryField
from django.db import models

from AdoptSquad.pets.choices import PersonalityChoices


class PetBase(models.Model):
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
        blank=True,
        null=True,
        folder='adopt-squad/pet-pictures',
        format='png',
    )

    personality = models.CharField(
        max_length=50,
        choices=PersonalityChoices.choices,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Dog(PetBase):
    leash_trained = models.BooleanField()


class Cat(PetBase):
    pass

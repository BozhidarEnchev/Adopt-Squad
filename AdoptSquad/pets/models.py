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

    pet_picture = models.ImageField(
        upload_to='adopt-squad/pet-pictures/',
        blank=True,
        null=True,
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

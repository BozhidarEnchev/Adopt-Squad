from django.contrib import admin
from AdoptSquad.pets.models import Dog, Cat


@admin.register(Dog)
class AdminDog(admin.ModelAdmin):
    fields = ['name', ('years', 'months'), 'personality', 'leash_trained', 'pet_picture']


@admin.register(Cat)
class AdminCat(admin.ModelAdmin):
    fields = ['name', ('years', 'months'), 'personality', 'pet_picture']


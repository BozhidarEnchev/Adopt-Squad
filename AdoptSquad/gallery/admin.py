from django.contrib import admin
from AdoptSquad.gallery.models import Photo


@admin.register(Photo)
class AdminPhoto(admin.ModelAdmin):
    list_display = ['photo']

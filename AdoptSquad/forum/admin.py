from django.contrib import admin
from AdoptSquad.forum.models import Post, Comment


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author',]
    list_filter = ['author',]


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['post', 'author',]
    list_filter = ['author',]

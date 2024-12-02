from django import forms

from AdoptSquad.common.mixins import FormFieldMixin
from AdoptSquad.forum.models import Post


class PostBaseForm(FormFieldMixin, forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']


class PostCreateForm(PostBaseForm):
    pass


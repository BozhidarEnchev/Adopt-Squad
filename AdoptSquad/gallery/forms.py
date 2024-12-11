from django import forms

from AdoptSquad.common.mixins import FormFieldMixin
from AdoptSquad.gallery.models import Photo


class PhotoBaseForm(FormFieldMixin, forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateForm(PhotoBaseForm):
    pass


class SearchBarForm(FormFieldMixin, forms.Form):
    pet = forms.CharField()

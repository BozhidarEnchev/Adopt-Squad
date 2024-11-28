from django import forms

from AdoptSquad.common.mixins import FormFieldMixin
from AdoptSquad.pets.models import Dog, Cat


class DogBaseForm(FormFieldMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['leash_trained'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Dog
        fields = '__all__'


class DogCreateForm(DogBaseForm):
    pass


class DogUpdateForm(DogBaseForm):
    pass


class CatBaseForm(FormFieldMixin, forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'


class CatCreateForm(CatBaseForm):
    pass


class CatUpdateForm(CatBaseForm):
    pass

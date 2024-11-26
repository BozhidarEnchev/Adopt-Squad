from django import forms

from AdoptSquad.pets.models import Dog, Cat


class DogCreateForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'


class CatCreateForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'


class DogUpdateForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'


class CatUpdateForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'

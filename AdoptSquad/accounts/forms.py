from cloudinary.forms import CloudinaryFileField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from AdoptSquad.accounts.models import AppUser
from AdoptSquad.common.mixins import FormFieldMixin


class AppUserCreationForm(FormFieldMixin, UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')


class AppUserChangeForm(FormFieldMixin, forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'profile_picture')


class AppUserAuthenticationForm(FormFieldMixin, AuthenticationForm):
    pass

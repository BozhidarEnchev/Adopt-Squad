from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from AdoptSquad.accounts.models import AppUser
from AdoptSquad.common.mixins import FormFieldMixin


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class AppUserChangeForm(FormFieldMixin, UserChangeForm):
    class Meta:
        model = AppUser
        fields = '__all__'


class AppUserAuthenticationForm(FormFieldMixin, AuthenticationForm):
    pass

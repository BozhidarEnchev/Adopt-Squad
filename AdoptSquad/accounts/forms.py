from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from AdoptSquad.accounts.models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = '__all__'

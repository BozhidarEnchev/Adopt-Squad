from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from AdoptSquad.accounts.models import User


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

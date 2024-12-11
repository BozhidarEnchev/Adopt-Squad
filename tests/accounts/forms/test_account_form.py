from django.contrib.auth import get_user_model
from django.test import TestCase

from AdoptSquad.accounts.forms import AppUserCreationForm

UserModel = get_user_model()


class TestPetForm(TestCase):
    def setUp(self):
        self.long_user = ('12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
                          '012345678901234567890123456789012345678901234567890123456789012345678901234567890')

    def test__username_too_long(self):
        form = AppUserCreationForm(data={'username': self.long_user, 'email': 'test@test.test', 'password': 'passwordtest1234'})
        self.assertFalse(form.is_valid())

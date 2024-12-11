from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestLoginView(TestCase):
    def setUp(self):
        self.user_credentials = {
            'username': 'test_user',
            'email': 'test_email@test.email',
            'password': 'test_password_123',
        }

        self.user = UserModel.objects.create_user(
            **self.user_credentials
        )

    def test__users_can_access_login_page(self):
        response = self.client.get(
            reverse('login')
        )
        self.assertEqual(response.status_code, 200)

    def test__successful_login_with_username(self):
        response = self.client.post(
            reverse('login'),
            data={
                'username': self.user_credentials['username'],
                'password': self.user_credentials['password']
            },
        )

        user = UserModel.objects.filter(username=self.user_credentials['username']).first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.email, self.user_credentials['email'])

    def test__successful_login_with_email(self):
        response = self.client.post(
            reverse('login'),
            data={
                'username': self.user_credentials['email'],
                'password': self.user_credentials['password'],
            }
        )

        user = UserModel.objects.filter(username=self.user_credentials['username']).first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.email, self.user_credentials['email'])


from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm


class TestUserRegistrationForm(TestCase):
    def test_can_create_new_user(self):
        form = UserRegistrationForm(
                    {'username': 'Bob', 
                    'email': 'bob@newuser.com', 
                    'password1': 'mynewpassword', 
                    'password2': 'mynewpassword'}
                    )
        self.assertTrue(form.is_valid())

    def test_can_create_new_user_with_wrong_password_confirm(self):
        form = UserRegistrationForm(
            {'username': 'Bob', 
            'email': 'bob@newuser.com', 
            'password1': 'mynewpassword', 
            'password2': 'anothernewpassword'}
            )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords do not match'])

class TestUserLoginForm(TestCase):
    c = Client()

    def test_user_can_login(self):
        form = UserLoginForm(
                    {'username': 'Bob', 
                    'password': 'mynewpassword'}
                    )
        self.assertTrue(form.is_valid())

    def test_user_can_login_without_password(self):
        form = UserLoginForm(
            {'username': 'test_user', 
            'password': ''}
            )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])




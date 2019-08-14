from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.forms import UserRegistrationForm, UserLoginForm


class TestAccountsViews(TestCase):

    def test_registration_page(self):
        response = self.client.get('/accounts/registration/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/registration.html')

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_profile_page(self):
        user = User.objects.create_user(
            'test_user',
            'test_user@mail.com',
            'example'
        )
        user.save()
        logged_in = self.client.login(username='test_user', password='example')
        response = self.client.get('/accounts/profile/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')



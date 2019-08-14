from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestCartViews(TestCase):
    c = Client()

    def setUp(self):
        user = User.objects.create_user(
            'test_user',
            'test_user@mail.com',
            'example'
        )
        user.save()
        logged_in = self.c.login(username='test_user', password='example')

    def test_view_cart(self):
        response = self.c.get('/cart/view_cart/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')  
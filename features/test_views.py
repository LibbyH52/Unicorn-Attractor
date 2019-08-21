from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from features.models import Feature, Comment


class TestFeatureViews(TestCase):
    """
    List of tests to be run against
    the views for the features app
    """
    c = Client()

    def setUp(self):
        user = User.objects.create_user(
            'test_user',
            'test_user@mail.com',
            'example'
        )
        user.save()
        logged_in = self.c.login(username='test_user', password='example')

    def test_get_features(self):
        response = self.c.get('/features/get_features/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/allfeatures.html')

    def test_feature_description_page(self):
        user = User(username='Marie')
        user.save()
        feature = Feature.objects.create(
            name='New feature',
            details='Yet another one',
            requested_by=user)
        feature.save()
        response = self.c.get('/features/{0}/'.format(feature.id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/featuredescription.html')

    def test_new_feature_page(self):
        user = User(username='Marie')
        user.save()
        feature = Feature.objects.create(
            name='A New Feature',
            details='I want this',
            requested_by=user)
        feature.save()
        response = self.c.get('/features/new_feature/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(feature, Feature))
        self.assertTemplateUsed(response, 'features/addfeature.html')

    def test_edit_feature_page(self):
        user = User(username='Marie')
        user.save()
        feature = Feature.objects.create(
            name='New feature',
            details='Yet another one',
            requested_by=user
            )
        feature.save()
        response = self.c.get('/features/{0}/edit_feature/'.format(feature.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/addfeature.html')

    def test_edit_feature_page_for_item_that_does_not_exist(self):
        response = self.c.get('features/{1}/edit_feature')
        self.assertEqual(response.status_code, 404)

    def test_add_feature_comment_page(self):
        user = User(username='Marie')
        user.save()
        feature = Feature.objects.create(
            name='New feature',
            details='Yet another one',
            requested_by=user)
        feature.save()
        comment = Comment.objects.create(
            comment='I have this feature too',
            author=user,
            feature=feature
        )
        comment.save()
        response = self.c.get(
            '/features/{0}/add_feature_comment/'.format(feature.id)
            )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(comment, Comment))
        self.assertTemplateUsed(response, 'features/addfeaturecomment.html')

    def test_edit_feature_comment_page(self):
        user = User(username='Marie')
        user.save()
        feature = Feature.objects.create(
            name='New feature',
            details='Yet another one',
            requested_by=user)
        feature.save()
        comment = Comment.objects.create(
            comment='I have this feature too',
            author=user,
            feature=feature)
        comment.save()
        response = self.c.get(
            '/features/{0}/edit_feature_comment/'.format(comment.id)
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/addfeaturecomment.html')

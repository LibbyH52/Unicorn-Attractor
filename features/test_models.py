from django.test import TestCase
from .models import Feature, Comment


class FeatureModelTest(TestCase):
    """
    List of tests to be run against
    the Features model
    """
    def test_str(self):
        feature = Feature(name='New Feature')
        self.assertEqual(str(feature), feature.name)


class CommentModelTest(TestCase):
    """
    Test to be run against
    the Comment model
    """
    def test_str(self):
        comment = Comment(comment='I want this too')
        self.assertEqual(str(comment), comment.comment)

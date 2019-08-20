from django.test import TestCase
from bugs.forms import AddBugForm, AddBugCommentForm


class TestAddBugForm(TestCase):
    def test_can_create_bug_with_missing_data(self):
        form = AddBugForm({'title': 'A New Bug', 'details': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['details'], [u'This field is required.'])


class TestAddBugCommentForm(TestCase):
    def test_can_create_bug_with_missing_data(self):
        form = AddBugCommentForm({'comment': ' '})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])

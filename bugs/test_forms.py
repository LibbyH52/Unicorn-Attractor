from django.test import TestCase
from bugs.forms import AddBugForm, AddCommentForm


class TestAddBugForm(TestCase):
    def test_can_create_bug_with_missing_data(self):
        form = AddBugForm({"title": "A New Bug", "details": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['details'], [u'This field is required.'])


class TestAddCommentForm(TestCase):
    def test_can_create_bug_with_missing_data(self):
        form = AddCommentForm({"comment": " "})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])

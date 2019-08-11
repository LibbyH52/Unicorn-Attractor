from django.test import TestCase, Client
from django.utils import timezone
from .models import Bug, Comment


class BugTest(TestCase):
    def test_string_representation(self):
        bug = Bug(title="Yet another one")
        self.assertEqual(str(bug), bug.title)


class CommentModelTest(TestCase):
    def test_string_representation(self):
        comment = Comment(comment="I am having the same problem")
        self.assertEqual(str(comment), comment.comment)

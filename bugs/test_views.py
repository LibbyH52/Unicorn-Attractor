from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from django.shortcuts import get_object_or_404
from bugs.models import Bug, Comment


class TestBugsViews(TestCase):

    c = Client()

    def setUp(self):
        """
        Set up method for unit testing the features app.
        Instance of User, Bug and Comment created
        here and called in tests.
        """
        user = User.objects.create_user(
            'test_user',
            'test_user@mail.com',
            'example'
        )
        user.save()
        bug = Bug.objects.create(
            title='New bug',
            details='Yet another one',
            author=user
            )
        bug.save()
        comment = Comment.objects.create(
            comment='I have this bug too',
            author=user,
            bug=bug
        )
        comment.save()
        logged_in = self.c.login(username='test_user', password='example')

    def test_show_bugs_page(self):
        response = self.c.get('/bugs/show_bugs/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs/allbugs.html')

    def test_bug_description_page(self):
        bug = Bug.objects.get(id=1)
        response = self.c.get('/bugs/{0}/'.format(bug.id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs/bugdescription.html')

    def test_add_bug_page(self):
        bug = Bug.objects.get(id=1)
        response = self.c.get('/bugs/add_bug/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(bug, Bug))
        self.assertTemplateUsed(response, 'bugs/addbug.html')

    def test_POST_add_bug_page(self):
        response = self.client.post("/bugs/add_bug/", {
            'title': 'A new bug',
            'details': 'This is a bug that I found'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_edit_bug_page(self):
        bug = Bug.objects.get(id=1)
        response = self.c.get('/bugs/{0}/edit_bug/'.format(bug.id))
        self.assertEqual(response.status_code, 200)

    def test_edit_bug_page_for_item_that_does_not_exist(self):
        response = self.c.get('bugs/{1}/edit_bug')
        self.assertEqual(response.status_code, 404)
    
    def test_delete_bug_page(self):
        bug = Bug.objects.get(id=1)
        response = self.c.get(
                              '/bugs/{0}/delete_bug/'
                              .format(bug.id)
                              )
        self.assertEqual(response.status_code, 302)

    def test_add_bug_comment_page(self):
        bug = Bug.objects.get(id=1)
        response = self.c.get('/bugs/{0}/add_bug_comment/'.format(bug.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs/addbugcomment.html')
    
    def test_POST_add_bug_comment_page(self):
        bug = Bug.objects.get(id=1)
        response = self.client.post("/bugs/{0}/add_bug_comment/".format(bug.id), {
            'comment': 'This would be a good feature'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_edit_bug_comment_page(self):
        comment = Comment.objects.get(id=1)
        response = self.c.get('/bugs/{0}/edit_bug_comment/'.format(comment.id))
        self.assertEqual(response.status_code, 200)

    def test_edit_comment_page_for_item_that_does_not_exist(self):
        response = self.c.get('bugs/{1}/edit_bug_comment')
        self.assertEqual(response.status_code, 404)

    def test_delete_comment_page_for_item_that_does_not_exist(self):
        response = self.c.get('bugs/{1}/delete_bug_comment')
        self.assertEqual(response.status_code, 404)

    def test_delete_bug_comment_page(self):
        comment = Comment.objects.get(id=1)
        response = self.c.get('/bugs/{0}/delete_bug_comment/'.format(comment.id))
        self.assertEqual(response.status_code, 302)
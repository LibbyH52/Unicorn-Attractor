from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bug(models.Model):
    """
    Creates a single bug report in the database
    """
    title = models.CharField(max_length=100)
    details = models.TextField()
    DONE = 'DONE'
    DOING = 'DOING'
    TODO = 'To Do'
    fix_status_choices =[
        (DONE, 'Done'),
        (DOING, 'Doing'),
        (TODO, 'To Do'),
        ]
    fix_status = models.CharField(max_length=10, choices=fix_status_choices, default='To Do')
    posted_on = models.DateField(null=True, blank=True, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateField(null=True, blank=True, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment

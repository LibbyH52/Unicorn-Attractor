from django.db import models
from django.utils import timezone

class Bug(models.Model):
    """
    Creates a single bug report in the database
    """
    title = models.CharField(max_length=100)
    details = models.TextField()
    FIXED = 'Fixed'
    FIXING = 'Fixing'
    TODO = 'To Do'
    fix_status_choices =[
        (FIXED, 'Fixed'),
        (FIXING, 'Fixing'),
        (TODO, 'To Do'),
        ]
    fix_status = models.CharField(max_length=10, choices=fix_status_choices, default='To Do')
    posted_on = models.DateField(null=True, blank=True, default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=300)
    posted_on = models.DateField(null=True, blank=True, default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

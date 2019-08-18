from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feature(models.Model):
    """
    Model for a single feature.
    """
    name = models.CharField(max_length=100)
    details = models.TextField()
    posted_on = models.DateTimeField(null=True, blank=True, default=timezone.now)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Done = 'Done'
    Doing = 'Doing'
    ToDo = 'ToDo'
    PHASE_OF_DEVELOPMENT_CHOICES =[
        (Done, 'Done'),
        (Doing, 'Doing'),
        (ToDo, 'ToDo'),
        ]
    phase_of_development = models.CharField(max_length=6, choices=PHASE_OF_DEVELOPMENT_CHOICES, default='ToDo')
    upvote = models.IntegerField(default=0)
    vote_price = models.DecimalField(max_digits=4, decimal_places=2, default=10.00)

    def __str__(self):
        return self.name

"""
Code for comment model obtained from Django Girls                              https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/
"""

class Comment(models.Model):
    """
    Creates a model to allow a user to comment
    on an individual feature request.
    """
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    posted_on = models.DateTimeField(null=True, blank=True, default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return self.comment

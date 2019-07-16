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
    views = models.IntegerField(default=0)
    upvote = models.IntegerField(default=0)

    def __str__(self):
        return self.name

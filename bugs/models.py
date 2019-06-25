from django.db import models
from django.utils import timezone

class Bug(models.Model):
    """
    A single bug report
    """
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=300)
    published_date = models.DateField(null=True, blank=True, default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=300)
    published_date = models.DateField(null=True, blank=True, default=timezone.now)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

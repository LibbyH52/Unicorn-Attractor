from django import forms
from .models import Bug, Comment


class AddBugForm(forms.ModelForm):
    """
    Creates a form to allow a user to
    add a bug report
    """
    class Meta:
        model = Bug
        fields = ('title', 'details')


class AddBugCommentForm(forms.ModelForm):
    """
    Creates a form to allow a user to
    comment on a bug report
    """
    class Meta:
        model = Comment
        fields = ('comment',)

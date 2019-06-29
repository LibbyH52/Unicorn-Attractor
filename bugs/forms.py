from django import forms
from .models import Bug, Comment

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'details')

class BugCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
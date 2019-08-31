from django import forms
from .models import Feature, Comment


class AddFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('name', 'details')


class AddFeatureCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

from django import forms
from .models import Feature


class AddFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('name', 'details')
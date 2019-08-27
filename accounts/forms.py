from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    """
    A form to allow new users to register
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """
        Function to validate email and user name of new users
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u
                                        'A user with that email already exists'
                                        )
        return email

    def clean_password2(self):
        """
        Function to validate password of new users
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class UserLoginForm(forms.Form):
    """
    Form used to log users in
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

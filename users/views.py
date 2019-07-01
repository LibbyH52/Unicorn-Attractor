from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    """
    Renders a page with a registration form,
    so users can sign up for the site
    """
    form = UserCreationForm()
    return render(request, 'users/registration.html', {'form':form})

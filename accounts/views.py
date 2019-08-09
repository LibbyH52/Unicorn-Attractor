from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from bugs.models import Bug
from features.models import Feature


def registration(request):
    """
    Renders a page with a registration form
    so users can sign up for the site
    """
    if request.user.is_authenticated:
        return redirect(reverse('login'))

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            messages.success(request, f"Account created for {username}.")
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


def user_profile(request):
    """
    Profile page for the logged in user.
    """
    user = User.objects.get(username=request.user.username)
    bugs = Bug.objects.filter(author=user)
    features = Feature.objects.filter(requested_by=user)
    return render(request, "accounts/profile.html", {"profile": user, 'bugs': bugs, 'features': features})


def login(request):
    """
    Creates a view to allow users to login
    """
    if request.user.is_authenticated:
        return redirect('show_bugs')
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('user_profile'))
            else:
                form.add_error(None, "Your username or password is incorrect")
    else:
        form = UserLoginForm
    return render(request, 'accounts/login.html', {'form': form})


@login_required()
def logout(request):
    """
    Allows a user to logout
    """
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))

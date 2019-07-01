from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def registration(request):
    """
    Renders a page with a registration form
    so users can sign up for the site
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            messages.success(request, f"Account successfully created for {username}")
            return redirect("show_bugs")
    
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form':form})

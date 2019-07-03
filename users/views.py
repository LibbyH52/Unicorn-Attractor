from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserRegistrationForm, UserLoginForm



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
            return redirect('login.html')
    
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form':form})

def login(request):
    """
    Creates a view to allow users to login
    """
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
            else:
                form.add_error(None, "Your username or password is incorrect")
            return redirect('show_bugs')
    else:
        form = UserLoginForm
    return render(request, 'login.html', {'form':form})

def logout(request):
    """
    Allows a user to logout 
    """
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('registration'))
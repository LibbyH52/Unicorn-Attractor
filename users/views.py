from django.shortcuts import render, redirect
from django.contrib import messages
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
            return redirect('users/login.html')
    
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form':form})

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
    return render(request, 'users/login.html', {'form':form})

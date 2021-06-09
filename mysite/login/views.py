from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm


# Create your views here.
def register(request):
    """Creates an account for the user or redirects them to the login page."""

    if request.method == 'POST':
        # Fill form with user details
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create an account but don't save
            new_user = user_form.save(commit=False)
            # Save the password to the new user
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the account
            new_user.save()
            return render(request, 'login/dashboard.html',
                          {'new_user': new_user})
        else:
            messages.error(request, 'Invalid account')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html',
                  {'user_form': user_form})


def login_request(request):
    """Authenticates User login"""

    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        # Validate form
        if login_form.is_valid():
            # Clean data
            cd = login_form.cleaned_data
            # Authenticate user with saved data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                # Backend credential authentication successful
                if user.is_active:
                    # Login user
                    login(request, user)
                    # Display message
                    messages.success(request, 'Login successful')
                    return render(request, 'login/dashboard.html')
                else:
                    messages.error(request, 'Disabled account')
            else:
                # Backend credential authentication successful
                messages.info(request, 'Login unsuccessful')
    else:
        login_form = UserLoginForm()
    return render(request, 'login/login.html', {'login_form': login_form})


def logout_request(request):
    """Logs out user and redirects to login page."""

    logout(request)
    messages.info(request, 'Logout successful')
    return redirect('login:login')


@login_required
def dashboard(request):
    return render(request, 'login/dashboard.html')

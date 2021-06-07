from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserLoginForm


# Create your views here.
def create_account(request):
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
        # else:
        #     # User exits.
        #     if user_form.cleaned_data['username']:
        #         return HttpResponse('Username already exists')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'signup/login.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            # Save info
            cd = login_form.cleaned_data
            # Authenticate user with saved data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                # Backend credential authentication successful
                pass
            else:
                # Backend credential authentication unsuccessful
                pass
    else:
        login_form = UserLoginForm()
    return render(request, 'login/login.html', {'login_form': login_form})


def dashboard(request):
    return render(request, 'login/dashboard.html')

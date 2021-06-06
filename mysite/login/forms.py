from django import forms
from django.contrib.auth.models import User

from .models import Accounts


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = Accounts
        fields = ('username', 'email')

    def clean_password2(self):
        """Validates if both passwords match."""

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserLoginForm(forms.Form):
    pass

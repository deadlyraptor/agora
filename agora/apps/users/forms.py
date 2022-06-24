from django import forms

from allauth.account.forms import SignupForm


class SignupForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='First name',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, label='Last name',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last name'}))

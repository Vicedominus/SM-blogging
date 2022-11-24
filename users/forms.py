from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-sm'})


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-sm'})


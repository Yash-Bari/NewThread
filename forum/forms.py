from django import forms
from .models import Thread, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

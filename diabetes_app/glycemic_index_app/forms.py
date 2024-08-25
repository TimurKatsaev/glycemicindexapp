from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Note

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'glycemia', 'bread_units']
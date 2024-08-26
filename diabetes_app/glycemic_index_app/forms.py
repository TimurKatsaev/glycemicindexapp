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

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'glycemia', 'bread_units', 'glycemic_index', 'general_gi', 'general_rcg', 'graph']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'form-name',
                'placeholder': 'Название записи',
                'name': 'title',
                'type': 'text',
                'required': ''
            }),
            'content': forms.Textarea(attrs={
                'id': 'form-desc',
                'placeholder': 'Описание',
                'name': 'desc',
                'type': 'text',
                'required': ''
            }),
            'glycemia': forms.TextInput(attrs={
                'id': 'form-clycemia',
                'placeholder': 'Ммоль/л',
                'name': 'glycemia',
                'type': 'text',
                'required': ''
            }),
            'bread_units': forms.TextInput(attrs={
                'id': 'form-XE',
                'placeholder': 'ХЕ',
                'name': 'bu',
                'type': 'text',
                'required': ''
            }),
            'glycemic_index': forms.HiddenInput(attrs={
                'id': 'actual-gi',
            }),
            'general_gi': forms.HiddenInput(attrs={
                'id': 'avg-gi',
            }),
            'general_rcg': forms.HiddenInput(attrs={
                'id': 'avg-rcg',
            }),
            'graph': forms.HiddenInput(attrs={
                'id': 'graph',
            }),
        }
    # glycemic_index = forms.CharField(required=False)
    # general_gi = forms.CharField(required=False)
    # general_rcg = forms.CharField(required=False)
    # graph = forms.CharField(required=False)
    # user = forms.CharField(required=False)
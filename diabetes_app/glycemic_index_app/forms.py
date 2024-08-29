from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

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
                'id': 'form-glycemia',
                'placeholder': 'Ммоль/л',
                'name': 'glycemia',
                'type': 'number',
                'required': '',
                'min': '1',
                'max': '25',
                'step': '0.01'
            }),
            'bread_units': forms.TextInput(attrs={
                'id': 'form-XE',
                'placeholder': 'ХЕ',
                'name': 'bu',
                'type': 'number',
                'required': '',
                'step': '0.01'
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

class EditingForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'glycemia', 'bread_units', 'glycemic_index', 'general_gi', 'general_rcg', 'graph']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'detail-input title-input',
                'placeholder': 'Название записи',
                'name': 'title',
                'type': 'text',
                'required': ''
            }),
            'content': forms.Textarea(attrs={
                'class': 'detail-input main-desc',
                'placeholder': 'Описание',
                'name': 'desc',
                'required': ''
            }),
            'glycemia': forms.TextInput(attrs={
                'class': 'detail-glycemia detail-input',
                'id': 'form-glycemia',
                'placeholder': 'Ммоль/л',
                'name': 'glycemia',
                'type': 'number',
                'required': '',
                'min': '1',
                'max': '25',
                'step': '0.01'
            }),
            'bread_units': forms.TextInput(attrs={
                'class': 'detail-glycemia detail-input',
                'placeholder': 'ХЕ',
                'id': 'form-XE',
                'name': 'bread_units',
                'type': 'number',
                'required': '',
                'step': '0.01'
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
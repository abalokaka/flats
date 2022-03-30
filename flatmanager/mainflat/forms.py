from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import TextInput, Textarea, ModelForm

from .models import Flat
from django import forms


def imghdr(attrs):
    pass


class FlatForm(ModelForm):
    class Meta:
        model = Flat
        fields = ['title', 'flat', 'image']
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите название"
        }),
            'flat': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
        }),
            'image': imghdr(attrs={
                'class': 'form-control',
                'placeholder': "Добавте фото"
        })
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)
    rating = forms.IntegerField(label='Score(1-10)', validators=[MinValueValidator(0), MaxValueValidator(10)])

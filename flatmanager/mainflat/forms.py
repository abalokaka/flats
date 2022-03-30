from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Flat
from django import forms



def imghdr(attrs):
    pass


class FlatForm(forms.Form):
    name = forms.CharField(label='Введите название', max_length=255)
    developer = forms.CharField(label='Developer', max_length=255)
    publisher = forms.CharField(label='Publisher', max_length=255)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.ImageField()


class LoginForm(FlatForm):
    username = forms.CharField(label='Login')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(FlatForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)
    rating = forms.IntegerField(label='Score(1-10)', validators=[MinValueValidator(0), MaxValueValidator(10)])

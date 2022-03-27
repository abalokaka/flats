from .models import Flat
from django.forms import ModelForm, TextInput, Textarea


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
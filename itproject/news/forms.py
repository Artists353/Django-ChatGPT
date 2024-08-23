from django.db.models import TextField

from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'announcement', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            "announcement": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
        }

from .models import *
from django.forms import ModelForm, TextInput, NumberInput

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'sum']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'sum': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму',
                'min': 1,
                'max': 1_000_000
            })
        }

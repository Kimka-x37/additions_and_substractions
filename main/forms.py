from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Form
from django.forms import CharField

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ник'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            })
        }
class LoginForm(Form):
    username = CharField(
        max_length=150,
        required=True, 
        widget=TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите ник'
                })
    )
    password = CharField(
        max_length=128,
        required=True, 
        widget=TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите пароль'
                })
    )
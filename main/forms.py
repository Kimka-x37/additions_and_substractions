from django.contrib.auth.models import User
from django.forms import TextInput, Form, PasswordInput
from django.forms import CharField
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ник'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ник'
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
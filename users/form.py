from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Введите Email",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label="Введите логин",
        required=True,
        help_text='Нельзя вводить символы: "@, /, ?"',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(label="Введите пароль",
                                required=True,
                                help_text="Пароль должен быть высокой сложности",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
                                )
    password2 = forms.CharField(label="Подтвердите пароль",
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Введите повторно пароль'})
                                )

    User._meta.get_field('email')._unique = True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label="Введите Email",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label="Введите логин",
        required=True,
        help_text='Нельзя вводить символы: "@, /, ?"',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    User._meta.get_field('email')._unique = True


class UserImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']

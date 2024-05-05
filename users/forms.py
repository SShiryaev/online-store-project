from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(UserCreationForm, StyleFormMixin):
    """Форма регистрации пользователя"""

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserProfileForm(UserChangeForm, StyleFormMixin):
    """Форма редактирования профиля пользователя"""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country',)

    def __init__(self, *args, **kwargs):
        # скрываем информационное сообщение о пароле в форме

        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

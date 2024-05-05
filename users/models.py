from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя
    с наследованием от AbstractUser
    исключением поля username
    и переопределением USERNAME_FIELD на поле email
    """

    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=80, **NULLABLE, verbose_name='страна')

    token = models.CharField(max_length=100, **NULLABLE, verbose_name='токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Пользователь ({self.email})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


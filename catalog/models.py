from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель категории (Типа) продукта (СЗР)"""

    name = models.CharField(max_length=50, **NULLABLE, verbose_name='Наименование')
    description = models.TextField(max_length=250, **NULLABLE, verbose_name='Описание')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Модель продукта (СЗР). Связанна с моделью Category (Тип) с отношением One to many (Один ко многим)"""

    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=8, decimal_places=2, **NULLABLE, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, **NULLABLE, verbose_name='Дата последнего изменения')

    in_stock = models.BooleanField(default=True, verbose_name='в наличии')
    seller = models.ForeignKey(User, **NULLABLE, on_delete=models.SET_NULL, verbose_name='продавец')
    is_published = models.BooleanField(default=False, verbose_name='опубликован')

    def __str__(self) -> str:
        return f'Продукт: {self.name} | Тип: {self.category.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('cancel_publication', 'Can cancel publication',),
            ('edit_description', 'Can edit description',),
            ('change_category', 'Can change category',),
        ]


class Contacts(models.Model):
    """Модель контактов компании (можно было сделать статикой)"""

    address = models.CharField(max_length=500, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    email_address = models.EmailField(max_length=70, verbose_name='Email')

    def __str__(self) -> str:
        return f'Адрес: {self.address} | Номер телефона: {self.phone_number} | Email: {self.email_address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Feedback(models.Model):
    """Модель контактов клиентов"""

    name = models.CharField(max_length=150, verbose_name='Имя')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    message = models.TextField(max_length=300, **NULLABLE, verbose_name='Сообщение')

    def __str__(self) -> str:
        return f'Имя: {self.name} | Номер телефона: {self.phone_number}'

    class Meta:
        verbose_name = 'контакты клиента'
        verbose_name_plural = 'контакты клиента'


class Version(models.Model):
    """
    Модель версии продукта (в данном случае номера гос. регистрации/окончания регистрации в РФ).
    Связанна с моделью Product (СЗР) с отношением One to many (Один ко многим)
    """

    product = models.ForeignKey(Product, related_name='version', on_delete=models.CASCADE, verbose_name='продукт')
    number = models.DateField(**NULLABLE, verbose_name='окончание регистрации')
    name = models.CharField(max_length=150, verbose_name='номер гос. регистрации')
    is_current = models.BooleanField(default=True, verbose_name='актуальная')

    def __str__(self):
        return f'Номер гос. регистрации: {self.name} | Окончание регистрации: {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

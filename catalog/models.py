from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, **NULLABLE, verbose_name='Наименование')
    discription = models.TextField(max_length=250, **NULLABLE, verbose_name='Описание')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    discription = models.TextField(max_length=250, **NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=8, decimal_places=2, **NULLABLE, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, **NULLABLE, verbose_name='Дата последнего изменения')

    in_stock = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self) -> str:
        return f'Продукт: {self.name} | Тип: {self.category.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contacts(models.Model):
    address = models.CharField(max_length=500, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    email_address = models.EmailField(max_length=70, verbose_name='Email')

    def __str__(self) -> str:
        return f'Адрес: {self.address} | Номер телефона: {self.phone_number} | Email: {self.email_address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    message = models.TextField(max_length=300, **NULLABLE, verbose_name='Сообщение')

    def __str__(self) -> str:
        return f'Имя: {self.name} | Номер телефона: {self.phone_number}'

    class Meta:
        verbose_name = 'контакты клиента'
        verbose_name_plural = 'контакты клиента'

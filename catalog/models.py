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

    def __str__(self) -> str:
        return f'Продукт: {self.name} | Категория {self.category.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

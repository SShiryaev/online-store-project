# Generated by Django 5.0.3 on 2024-05-06 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('cancel_publ', 'Can cancel publication'), ('edit_descr', 'Can edit description'), ('change_category', 'Can change category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]

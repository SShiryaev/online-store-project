import json
import os

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(os.path.join('data.json'), encoding='utf-8') as file:
            data_json = file.read()
        models = json.loads(data_json)
        categories_list = []
        for model in models:
            if model['model'] == 'catalog.category':
                categories_list.append(model)
        return categories_list

    @staticmethod
    def json_read_products():
        with open(os.path.join('data.json'), encoding='utf-8') as file:
            data_json = file.read()
        models = json.loads(data_json)
        products_list = []
        for model in models:
            if model['model'] == 'catalog.product':
                products_list.append(model)
        return products_list

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in self.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'],
                         discription=category['fields']['discription'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in self.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        discription=product['fields']['discription'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)

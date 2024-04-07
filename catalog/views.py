from django.shortcuts import render
from catalog.models import Product, Contacts


def home(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Главная',
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    context = {
        'contacts': Contacts.objects.all(),
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'product': Product.objects.get(pk=pk),
        'title': 'Продукт',
    }
    return render(request, 'catalog/product.html', context)

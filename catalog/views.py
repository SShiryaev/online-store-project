from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from catalog.models import Product, Contacts


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'discription', 'image', 'category', 'price',)
    success_url = reverse_lazy('catalog:list_product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'discription', 'image', 'category', 'price',)
    success_url = reverse_lazy('catalog:list_product')


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list_product')


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

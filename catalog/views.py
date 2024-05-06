from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm, FeedbackForm, ProductModeratorForm
from catalog.models import Product, Contacts, Feedback, Version


class ProductListView(ListView):
    """Представление отображения списка продуктов (СЗР)"""

    model = Product

    def get_context_data(self, **kwargs):
        # отображение только актуальных версий у продуктов (СЗР)

        context_data = super().get_context_data(**kwargs)
        context_data['product_list'] = Product.objects.all()
        current_versions = Version.objects.filter(is_current=True)
        context_data['current_versions'] = current_versions
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Представление пользовательского интерфейса для добавления продукта (СЗР)"""

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')

    def get_context_data(self, **kwargs):
        # используем форму ProductForm для POST запроса

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        # продукт присваивается создавшему его пользователю

        product = form.save()
        user = self.request.user
        product.seller = user
        product.save()
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid() and formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Представление пользовательского интерфейса для редактирования продукта (СЗР)"""

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')

    def get_context_data(self, **kwargs):
        # метод позволяет использовать форму ProductForm для POST запроса

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        # валидация формы и формсета

        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid() and formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user == self.object.seller:
            return ProductForm
        elif user.has_perm('catalog.cancel_publication') and \
                user.has_perm('catalog.edit_description') and \
                user.has_perm('catalog.change_category'):
            return ProductModeratorForm
        else:
            return PermissionDenied


class ProductDetailView(DetailView):
    """Представление пользовательского интерфейса для детального просмотра продукта (СЗР)"""

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Product

    def get_context_data(self, **kwargs):
        # показывает только актуальные версии у продуктов (СЗР)

        context_data = super().get_context_data(**kwargs)
        current_version = Version.objects.filter(is_current=True).first()
        context_data['current_version'] = current_version
        return context_data


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Представление пользовательского интерфейса для удаления продукта (СЗР) через подтверждение"""

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"
    model = Product
    success_url = reverse_lazy('catalog:list_product')


class FeedbackCreateView(CreateView):
    """Представление пользовательского интерфейса для создания сущности контактов клиента"""

    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('catalog:contacts')

    def get_context_data(self, **kwargs):
        # отображение контактов компании на странице

        context_data = super().get_context_data(**kwargs)
        context_data['object'] = Contacts.objects.get(pk=1)
        return context_data


def toggle_stock(request, pk):
    # можно изменить поле in_stock (в наличии) у сущности Product (СЗР) на странице со списком продуктов

    product_item = get_object_or_404(Product, pk=pk)
    if product_item.in_stock:
        product_item.in_stock = False
    else:
        product_item.in_stock = True

    product_item.save()

    return redirect(reverse('catalog:list_product'))

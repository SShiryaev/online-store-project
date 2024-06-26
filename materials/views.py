import os

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.forms import MaterialForm
from materials.models import Material


class MaterialCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление добавления материала (статьи)"""

    model = Material
    fields = ('title', 'body', 'slug', 'preview',)
    success_url = reverse_lazy('materials:list')
    permission_required = "materials.add_material"

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление редактирования материала (статьи)"""

    model = Material
    form_class = MaterialForm
    permission_required = "materials.change_material"

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    """Представление отображения списка материалов (статей)"""

    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail('Блог СЗР',
                      'Поздравляем, ваш материал достиг 100 просмотров!',
                      os.getenv('MY_EMAIL_HOST_USER'),
                      [os.getenv('MY_EMAIL_HOST_RECIPIENT')],
                      fail_silently=False,)
        return self.object


class MaterialDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление удаления материала (статьи)"""

    model = Material
    success_url = reverse_lazy('materials:list')
    permission_required = "materials.delete_material"

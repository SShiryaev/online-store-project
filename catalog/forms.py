from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'discription', 'image', 'category', 'price',)

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        name = self.cleaned_data['name']
        if name in forbidden_words:
            raise ValidationError('Это название запрещено, выберите другое')
        return name

    def clean_discription(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        discription = self.cleaned_data['discription']
        for word in forbidden_words:
            if discription.find(word) != -1:
                raise ValidationError('В описании присутствуют запрещенные слова, измените описание')
        return discription


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

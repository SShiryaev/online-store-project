from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
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


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

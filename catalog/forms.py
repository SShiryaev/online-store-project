from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from catalog.models import Product, Version, Feedback

FORBIDDEN_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)


class StyleFormMixin:
    """Миксин добавляющий стили Bootstrap для BooleanField и формы в целом"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения продукта СЗР"""

    class Meta:
        model = Product
        fields = ('name', 'discription', 'image', 'category', 'price',)

    def clean_name(self):
        # clean метод для валидации имени продукта
        # не позволяет добавить слова из множества FORBIDDEN_WORDS и рэйзит ошибку

        cleaned_data = self.cleaned_data['name']

        for word in FORBIDDEN_WORDS:
            if cleaned_data.lower().find(word) != -1:
                raise ValidationError('Это название запрещено, выберите другое')
        return cleaned_data

    def clean_discription(self):
        # clean метод для валидации описания продукта
        # не позволяет добавить слова из множества FORBIDDEN_WORDS и рэйзит ошибку

        cleaned_data = self.cleaned_data['discription']

        for word in FORBIDDEN_WORDS:
            if cleaned_data.lower().find(word) != -1:
                raise ValidationError('В описании присутствуют запрещенные слова, измените описание')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения версии продукта
    в данном случае номера гос. регистрации/окончания регистрации в РФ
    """

    class Meta:
        model = Version
        fields = '__all__'

    # def clean_is_current(self):
    #     cleaned_data = self.cleaned_data.get('is_current')
    #     current_version = Version.objects.filter(is_current=self.cleaned_data.get('is_current')).distinct()
    #     if cleaned_data and current_version:
    #         raise ValidationError('Актуальная версия может быть одна, снимите флаг с предыдущей')
    #     return cleaned_data


class FeedbackForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления контактных данных клиента"""

    class Meta:
        model = Feedback
        fields = '__all__'

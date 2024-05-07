from django import forms

from catalog.forms import StyleFormMixin
from materials.models import Material


class MaterialForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения статьи"""

    class Meta:
        model = Material
        fields = ('title', 'body', 'preview',)

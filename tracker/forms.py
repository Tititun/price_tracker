from django.forms import ModelForm
from django.forms import ValidationError

from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['url']
    
    def clean_url(self):
        url = self.cleaned_data['url']
        if 'ozon.ru' not in url:
            raise ValidationError('Ссылка должна быть на товар с ozon.ru')
        return url

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["url"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Ссылка на товар" })
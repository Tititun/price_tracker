from django.forms import ModelForm

from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['url']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["url"].widget.attrs.update(
            {"class": "form-control w-50", "placeholder": "Ссылка на товар" })
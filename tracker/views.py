from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.views.generic import ListView
from django.shortcuts import render, redirect

from .forms import ItemForm
from .models import Item


def main_page(request: HttpRequest):
    if request.method == 'POST':
        url = request.POST.get('url')
        form = ItemForm(request.POST)
        
        if not request.session.get('items'):
            request.session['items'] = []
        request.session['items'].append(url)
        return redirect('/items')
    form = ItemForm(auto_id=False)
    return render(request, 'tracker/main.html', {'form': form})


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    
    def get_queryset(self):
        return super().get_queryset()

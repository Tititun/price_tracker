from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('items', views.ItemListView.as_view(), name='item-list'),
    path('', views.main_page, name='main')
]
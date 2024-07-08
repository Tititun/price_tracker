from urllib.parse import urlparse

from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=512)
    url = models.URLField(max_length=1024, null=False)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name[:100]} [{urlparse(self.url).hostname}]'
        

class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

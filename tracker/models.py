from urllib.parse import urlparse

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=512, null=False)
    url = models.URLField(max_length=1024, null=False)

    def __str__(self):
        return f'{self.name[:100]} [{urlparse(self.url).hostname}]'
        

class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)

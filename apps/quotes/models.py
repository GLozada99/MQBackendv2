from decimal import Decimal

from django.db import models
from django.utils import timezone

from apps.people.models import Client
from apps.products.models import Product


class Quote(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
    generated_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    closed_date = models.DateField(null=True, blank=True)
    taken = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    extra_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Quote for {self.client}, on {self.generated_date}. {self.extra_info}'


class Invoice(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.PROTECT)
    payment = models.DecimalField(max_digits=7, decimal_places=2)
    balance = models.DecimalField(max_digits=7, decimal_places=2)

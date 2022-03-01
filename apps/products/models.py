from decimal import Decimal

from django.db import models
from safedelete.models import SafeDeleteModel

from extras.mixins import UpdateMixin


class Product(SafeDeleteModel, UpdateMixin):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    picture = models.ImageField(upload_to='product_pics/')
    price = models.DecimalField(max_digits=4,
                                decimal_places=2, default=Decimal(0))
    availability = models.PositiveIntegerField(default=0)

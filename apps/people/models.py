from django.db import models
from safedelete.models import SafeDeleteModel

from extras.mixins import UpdateMixin


class Person(SafeDeleteModel, UpdateMixin):
    identification = models.CharField(max_length=11)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Client(Person):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

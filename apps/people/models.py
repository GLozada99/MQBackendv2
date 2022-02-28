from django.db import models
from mixins import UpdateMixin


class Person(models.Model, UpdateMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

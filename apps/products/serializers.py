from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.products.models import Product


class BasicProductSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(
        max_length=None, use_url=True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'availability', 'picture')

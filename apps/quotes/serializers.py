from rest_framework import serializers

from apps.products.serializers import BasicProductSerializer
from apps.quotes.models import Quote, Invoice
from apps.people.serializers import BasicClientSerializer


class BasicQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('client', 'products', 'due_date',
                  'closed_date', 'extra_info')


class ClientQuoteSerializer(serializers.ModelSerializer):
    client = BasicClientSerializer()

    class Meta:
        model = Quote
        fields = ('client',)


class ProductsQuoteSerializer(serializers.ModelSerializer):
    products = BasicProductSerializer(many=True)

    class Meta:
        model = Quote
        fields = ('products',)


class BasicInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('quote', 'payment', 'balance', 'date')


class QuoteInvoiceSerializer(serializers.ModelSerializer):
    quote = BasicQuoteSerializer
    
    class Meta:
        model = Invoice
        fields = ('quote', 'payment', 'balance', 'date')

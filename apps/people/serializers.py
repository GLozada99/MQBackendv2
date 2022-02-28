from rest_framework import serializers

from apps.people.models import Client


class BasicClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('identification', 'last_name', 'first_name',
                  'email', 'birth_date', 'phone_number', 'address')

from django.contrib import admin

from apps.people.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('identification', 'last_name', 'first_name', 'email', 'phone_number')


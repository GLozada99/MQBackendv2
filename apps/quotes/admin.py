from django.contrib import admin

from apps.quotes.models import Quote, Invoice


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('client', 'taken', 'cost',
                    'generated_date', 'due_date', 'closed_date')
    readonly_fields = ['cost']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('quote', 'payment', 'balance', 'date')

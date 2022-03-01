from django.contrib import admin

from apps.quotes.models import Quote, Invoice, ProductQuote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('client', 'taken', 'cost',
                    'generated_date', 'due_date', 'closed_date')
    readonly_fields = ['cost', 'current_balance']
    update_readonly_fields = ['products']
    create_readonly_fields = ['taken', 'closed']

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + (self.update_readonly_fields
                                       if obj else self.create_readonly_fields)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('quote', 'payment', 'balance', 'date')
    readonly_fields = ['balance']


@admin.register(ProductQuote)
class ProductQuoteAdmin(admin.ModelAdmin):
    list_display = ('product', 'quote', 'quantity')
    update_readonly_fields = ['product', 'quote', 'quantity']
    create_readonly_fields = []

    class Meta:
        unique_together = ('product', 'quote')

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + (self.update_readonly_fields
                                       if obj else self.create_readonly_fields)


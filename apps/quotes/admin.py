from django.contrib import admin

from apps.quotes.models import Quote, Invoice


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('client', 'taken', 'cost',
                    'generated_date', 'due_date', 'closed_date')
    readonly_fields = ['cost']
    update_readonly_fields = ['products']
    create_readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + (self.update_readonly_fields
                                       if obj else self.create_readonly_fields)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('quote', 'payment', 'balance', 'date')
    readonly_fields = ['balance']

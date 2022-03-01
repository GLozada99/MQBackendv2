from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from apps.quotes.models import Quote, Invoice


@receiver(m2m_changed, sender=Quote.products.through)
def apply_cost_quote(instance, **kwargs):
    instance.set_cost()


@receiver(post_save, sender=Quote)
def apply_sale_quote(instance, sender, **kwargs):
    former_instance = sender.objects.get(pk=instance.pk)
    if former_instance.taken != instance.taken:
        instance.update(current_balance=instance.cost)
        for item in instance.products.all():
            item.product.apply_sale()


@receiver(post_save, sender=Invoice)
def set_current_balance(instance, created, **kwargs):
    if created:
        new_balance = instance.quote.current_balance - instance.payment
        instance.quote.update(current_balance=new_balance)
        instance.update(balance=new_balance)

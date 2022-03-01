from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from apps.quotes.models import Quote


@receiver(m2m_changed, sender=Quote.products.through)
def apply_cost_quote(instance, **kwargs):
    instance.set_cost()


@receiver(post_save, sender=Quote)
def set_start_balance(instance, created, sender, **kwargs):
    former_instance = sender.objects.get(pk=instance.pk)
    if former_instance.taken != instance.taken:
        instance.update(current_balance=instance.cost)

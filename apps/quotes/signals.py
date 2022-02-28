from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.quotes.models import Quote


@receiver(m2m_changed, sender=Quote.products.through)
def apply_cost_quote(instance, **kwargs):
    instance.set_cost()

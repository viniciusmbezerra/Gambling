from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from MegaSena.models import Concourse


@receiver(post_save, sender=Concourse)
def create_concourse(sender, instance, created, *args, **kwargs):
    if created:
        instance.add_scheduled_bet()

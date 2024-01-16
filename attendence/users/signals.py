from django.db.models.signals import post_save     #  this is signal
from django.contrib.auth.models import User   # User sends the signal
from django.dispatch import receiver    # receiver
from . models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



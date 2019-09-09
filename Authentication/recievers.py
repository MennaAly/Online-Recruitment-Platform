from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('save user profile')
    try:
        instance.profile.save()
    except:
        Profile.objects.create(user=instance)

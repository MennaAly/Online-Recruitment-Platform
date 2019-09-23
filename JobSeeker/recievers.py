from django.dispatch import receiver
from django.db.models.signals import post_migrate
# from .apps import JobseekerConfig
from .models import CurrentLevel

# @receiver(post_migrate, sender=JobseekerConfig)
def populate_date(sender, instance, **kwargs):
    # file = open("curentlevel.txt", 'r')
    #
    # f = file.readlines()
    # for x in f:
    CurrentLevel.objects.create(level='x')

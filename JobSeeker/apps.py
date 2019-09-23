from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .recievers import populate_date

class JobseekerConfig(AppConfig):
    name = 'JobSeeker'

    def ready(self):
        post_migrate.connect(populate_date , sender=self)
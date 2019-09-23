from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from .views import CreateJobSeekerProfile
router = routers.SimpleRouter()
router.register(r'CreateJobSeekerProfile', CreateJobSeekerProfile)

urlpatterns = [
    url('', include(router.urls)),
]

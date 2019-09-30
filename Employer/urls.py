from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from .views import UpdateEmployerProfile
router = routers.SimpleRouter()

urlpatterns = [
    url(r'^update_employer_profile', UpdateEmployerProfile.as_view()),

]

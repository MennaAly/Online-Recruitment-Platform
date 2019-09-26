from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from .views import UpdateJobSeekerProfile
router = routers.SimpleRouter()

urlpatterns = [
    url(r'^update_jobseeker_profile', UpdateJobSeekerProfile.as_view()),

]

from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from .views import PostJob ,ApplyForJob
router = routers.SimpleRouter()
router.register(r'post_job', PostJob)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^apply_for_job',ApplyForJob.as_view())
]
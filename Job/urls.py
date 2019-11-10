from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from .views import PostJob ,ApplyForJob ,filterJobs , JobSeekerAndJobs
router = routers.SimpleRouter()
router.register(r'post_job', PostJob)
router.register(r'job_filter', filterJobs)
router.register(r'jobseeker_jobs',JobSeekerAndJobs)
# url(r'^job_filter', filterJobs.as_view()),

urlpatterns = [
    url('', include(router.urls)),
    url(r'^apply_for_job',ApplyForJob.as_view()),
]

from django.db import models
# standard
# django core
# third library
from django.contrib.auth.models import User
# your app
# Create your models here.
from Authentication.models import Profile


class CompanySize(models.Model):
    size = models.CharField(max_length=256)


class CompanyIndustry(models.Model):
    industry = models.CharField(max_length=256)


class EmployerProfile(models.Model):
    general_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256, null=True)
    company_phone = models.CharField(max_length=11, null=True)
    company_website = models.CharField(max_length=256, null=True)
    company_industry = models.ForeignKey(CompanyIndustry, on_delete=models.PROTECT, null=True)
    company_size = models.ForeignKey(CompanySize, on_delete=models.PROTECT, null=True)

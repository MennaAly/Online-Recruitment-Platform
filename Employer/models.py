from django.db import models
# from JobSeeker.models import Role
# standard
# django core
# third library
from django.contrib.auth.models import User
# your app
# Create your models here.
from Authentication.models import Profile
from MasterData.models import Role , CompanyIndustry ,CompanySize , Country


class ContactInfo(models.Model):
    username = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256, null=True)
    job_role = models.ForeignKey(Role,on_delete=models.PROTECT,null=True)
    mobile_number = models.CharField(max_length=256,null=True)

class EmployerProfile(models.Model):
    general_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    ContactInfo = models.OneToOneField(ContactInfo,on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=256, null=True)
    company_phone = models.CharField(max_length=11, null=True)
    company_website = models.CharField(max_length=256, null=True)
    company_industry = models.ForeignKey(CompanyIndustry, on_delete=models.PROTECT, null=True)
    company_size = models.ForeignKey(CompanySize, on_delete=models.PROTECT, null=True)
    country = models.ForeignKey(Country,on_delete=models.PROTECT,null=True)

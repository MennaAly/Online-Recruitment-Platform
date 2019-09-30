from django.db import models

# Create your models here.
class CurrentLevel(models.Model):
    level = models.CharField(max_length=255)


class JobType(models.Model):
    type = models.CharField(max_length=255)


class Role(models.Model):
    role = models.CharField(max_length=255)

class Country(models.Model):
    name = models.CharField(max_length=255,null=True)
    iso = models.CharField(max_length=225,null=True)
    nicename = models.CharField(max_length=225,null=True)
    iso3 = models.CharField(max_length=225,null=True)
    numcode = models.IntegerField(null=True)
    phonecode = models.IntegerField(null=True)

class SearchStatus(models.Model):
    status = models.CharField(max_length=255)

class YearsOfExpiernce(models.Model):
    num_of_years = models.CharField(max_length=256)


class CompanySize(models.Model):
    size = models.CharField(max_length=256)


class CompanyIndustry(models.Model):
    industry = models.CharField(max_length=256)

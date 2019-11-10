from django.db import models
from MasterData.models import CurrentLevel, JobType, Language, Role
from Employer.models import EmployerProfile

# Create your models here.
class Point(models.Model):
    point = models.CharField(max_length=256)


class Paragraph(models.Model):
    title = models.CharField(max_length=256,null=True,blank=True)
    points = models.ManyToManyField(Point)
    is_about_job = models.BooleanField(default=True,null=True,blank=True)
    is_job_requirement = models.BooleanField(default=False,null=True,blank=True)

# every field is null=true
class JobPost(models.Model):
    post_name = models.CharField(max_length=256)
    company = models.ForeignKey(EmployerProfile, on_delete=models.PROTECT)
    years_of_expierence = models.CharField(max_length=256,null=True,blank=True)
    job_roles = models.ManyToManyField(Role)
    career_level = models.ForeignKey(CurrentLevel, on_delete=models.PROTECT)
    # default Confidential
    salary = models.CharField(max_length=256,default='Confidential',null=True,blank=True)
    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT)
    languages = models.ManyToManyField(Language)
    vacancies = models.IntegerField(null=True,blank=True)
    pargraphs = models.ManyToManyField(Paragraph)
    is_active = models.BooleanField(default=True,null=True,blank=True)


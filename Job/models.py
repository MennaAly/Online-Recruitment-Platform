from django.db import models
from MasterData.models import CurrentLevel, JobType, Language, Role
from Employer.models import EmployerProfile
from JobSeeker.models import JobSeekerProfile


# Create your models here.
class Point(models.Model):
    point = models.CharField(max_length=256)


class Paragraph(models.Model):
    title = models.CharField(max_length=256)
    points = models.ManyToManyField(Point)


class JobDescription(models.Model):
    pargraphs = models.ManyToManyField(Paragraph)
    is_about_job = models.BooleanField(default=True)
    is_job_requirement = models.BooleanField(default=False)


class JobPost(models.Model):
    post_name = models.CharField(max_length=256)
    company = models.ForeignKey(EmployerProfile, on_delete=models.PROTECT)
    years_of_expierence = models.CharField(max_length=256)
    job_roles = models.ManyToManyField(Role)
    career_level = models.ForeignKey(CurrentLevel, on_delete=models.PROTECT)
    salary = models.CharField(max_length=256)
    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT)
    languages = models.ManyToManyField(Language)
    vacancies = models.IntegerField()
    job_description = models.ForeignKey(JobDescription, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    applicants = models.ManyToManyField(JobSeekerProfile)

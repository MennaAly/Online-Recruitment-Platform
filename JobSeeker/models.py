# standard library imports
# core django imorts
from django.db import models
# third party app imports
from django.contrib.auth.models import User
from Employer.models import CompanySize, CompanyIndustry
# imports from your app
from Authentication.models import Profile

# Create your models here.

gender_choices = {
    ('Male', 'Male'),
    ('Female', 'Female')
}

martial_status_choices = {
    ('Single', 'Single'),
    ('Married', 'Married'),
}

experience_type_choices = {
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
    ('Freelance/Project', 'Freelance/Project'),
    ('Internship', 'Internship'),
    ('Volunteering', 'Volunteering'),
    ('Student activity', 'Student activity')
}


class GeneralInfo(models.Model):
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    nationality = models.CharField(max_length=255)
    martial_status = models.CharField(max_length=10, choices=martial_status_choices, default='Single')
    num_of_dependencies = models.IntegerField()
    have_driving_license = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=15)


class CurrentLevel(models.Model):
    level = models.CharField(max_length=255)


class JobType(models.Model):
    type = models.CharField(max_length=255)


class Role(models.Model):
    role = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)


class SearchStatus(models.Model):
    status = models.CharField(max_length=255)


class Intersts(models.Model):
    current_level = models.OneToOneField(CurrentLevel, on_delete=models.PROTECT)
    job_type = models.ManyToManyField(JobType)
    role = models.ManyToManyField(Role)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    search_status = models.ForeignKey(SearchStatus, on_delete=models.PROTECT)


class Expirence(models.Model):
    expiernce_type = models.CharField(max_length=25, choices=experience_type_choices)
    job_title = models.CharField(max_length=225)
    job_role = models.ForeignKey(Role, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=225)
    '''
    auto_now  will be updated every time the save function called
    auto_now_add will be called in the create 
    '''
    from_date = models.DateField()
    is_work_there = models.BooleanField()
    description = models.CharField(max_length=256)
    career_level = models.OneToOneField(CurrentLevel, on_delete=models.PROTECT)
    company_size = models.ForeignKey(CompanySize, on_delete=models.PROTECT)
    company_industry = models.ForeignKey(CompanyIndustry, on_delete=models.PROTECT)
    starting_salary = models.IntegerField()
    ending_salary = models.IntegerField()


class YearsOfExpiernce(models.Model):
    num_of_years = models.CharField(max_length=256)


class Skill(models.Model):
    skill_name = models.CharField(max_length=256)
    profiency_rate = models.IntegerField()
    interest_rate = models.IntegerField()
    years_of_expiernce = models.ForeignKey(YearsOfExpiernce, on_delete=models.PROTECT)


class JobSeekerProfile(models.Model):
    '''
    one to one field is same as Foriegn key but the reverse relation of one to one will return just one object but the
    foreign key is for one to many
    user.profile => < profile :  ...>
    '''
    general_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    general_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, null=True)
    intersts = models.ForeignKey(Intersts, on_delete=models.CASCADE, null=True)
    experiences = models.ManyToManyField(Expirence)
    upload_cv = models.FilePathField(null=True)

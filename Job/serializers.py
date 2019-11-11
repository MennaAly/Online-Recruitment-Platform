from rest_framework import serializers
from Employer.models import EmployerProfile
from Employer.serializers import EmployerProfileSerializer
from JobSeeker.models import JobSeekerProfile, JobSeekerAndJobPosts
from MasterData.models import CurrentLevel, JobType, Role, Language
from MasterData.serializers import CurrentLevelSerializer, LanguageSerializer ,RoleSerializer,JobTypeSerializer
from .models import Point, Paragraph, JobPost


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['title', 'is_about_job', 'is_job_requirement']
        read_only_fields = ['id']


class JobPostSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=EmployerProfile.objects.all(), default=True,
                                                    source='company')
    career_level_id = serializers.PrimaryKeyRelatedField(queryset=CurrentLevel.objects.all(), default=False,
                                                         source='career_level')
    job_type_id = serializers.PrimaryKeyRelatedField(queryset=JobType.objects.all(), default=False, source='job_type')

    company_object = serializers.SerializerMethodField()

    job_role_set = serializers.SerializerMethodField()

    career_level_object = serializers.SerializerMethodField()

    job_type_object = serializers.SerializerMethodField()

    language_set = serializers.SerializerMethodField()

    is_about_job_set = serializers.SerializerMethodField()

    is_job_requirement_set = serializers.SerializerMethodField()

    number_of_applicants = serializers.SerializerMethodField()

    def get_company_object(self, obj):
         employer_profile = EmployerProfile.objects.filter(jobpost=obj).first()
         return EmployerProfileSerializer(employer_profile).data

    def get_job_role_set(self, obj):
        role = Role.objects.filter(jobpost=obj)
        return RoleSerializer(role,many=True).data

    def get_career_level_object(self, obj):
        current_level = CurrentLevel.objects.filter(jobpost=obj).first()
        return CurrentLevelSerializer(current_level).data

    def get_job_type_object(self, obj):
        job_type =  JobType.objects.filter(jobpost=obj).first()
        return JobTypeSerializer(job_type).data

    def get_language_set(self, obj):
        languages =  Language.objects.filter(jobpost=obj)
        return LanguageSerializer(languages,many=True).data

    def get_is_about_job_set(self, obj):
        is_about_paragraphs = Paragraph.objects.filter(jobpost=obj, is_about_job=True)
        return ParagraphSerializer(is_about_paragraphs,many=True).data

    def get_is_job_requirement_set(self, obj):
        is_job_requirement_paragraphs = Paragraph.objects.filter(jobpost=obj, is_job_requirement=True)
        return ParagraphSerializer(is_job_requirement_paragraphs,many=True).data

    def get_number_of_applicants(self, obj):
        return JobSeekerAndJobPosts.objects.filter(job_post=obj,is_applied_for=True).count()

    class Meta:
        model = JobPost
        fields = [
            'id',
            'post_name',
            'company_id',
            'years_of_expierence',
            'career_level_id',
            'job_type_id',
            'salary',
            'vacancies',
            'company_object',
            'job_role_set',
            'career_level_object',
            'job_type_object',
            'language_set',
            'is_about_job_set',
            'is_job_requirement_set',
            'number_of_applicants',
            'date'
        ]
        read_only_fields = ['id']

class JobPostMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields =[
            'id',
            'post_name',
        ]
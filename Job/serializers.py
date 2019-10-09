from rest_framework import serializers
from Employer.models import EmployerProfile
from MasterData.models import CurrentLevel, JobType
from .models import  Point, Paragraph, JobPost


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['title','is_about_job','is_job_requirement']
        read_only_fields = ['id']


class JobPostSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=EmployerProfile.objects.all(), default=True,
                                                    source='company')
    career_level_id = serializers.PrimaryKeyRelatedField(queryset=CurrentLevel.objects.all(), default=False,
                                                         source='career_level')
    job_type_id = serializers.PrimaryKeyRelatedField(queryset=JobType.objects.all(), default=False, source='job_type')

    class Meta:
        model = JobPost
        fields = [
            'post_name',
            'company_id',
            'years_of_expierence',
            'career_level_id',
            'job_type_id',
            'salary',
            'vacancies',
        ]
        read_only_fields = ['id']

from rest_framework import serializers

from Employer.models import CompanySize, CompanyIndustry
from .models import JobSeekerProfile, GeneralInfo, Intersts, Expirence, Skill, CurrentLevel, JobType, Role, Country, \
    SearchStatus, YearsOfExpiernce


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    years_of_expiernce_id = serializers.PrimaryKeyRelatedField(queryset=YearsOfExpiernce.objects.all(),
                                                               source='YearsOfExpiernce', required=False)

    class Meta:
        model = Skill
        fields = ['skill_name', 'profiency_rate', 'interest_rate', 'years_of_expiernce_id']
        read_only_fields = ['id']


class InterstsSerializer(serializers.ModelSerializer):
    current_level_id = serializers.PrimaryKeyRelatedField(queryset=CurrentLevel.objects.all(), source='CurrentLevel',
                                                          required=False)
    job_types = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), source='Country', required=False)
    search_status_id = serializers.PrimaryKeyRelatedField(queryset=SearchStatus.objects.all(), source='SearchStatus',
                                                          required=False)

    def get_job_types(self, obj):
        job_type_instances = JobType.objects.filter(Intersts=obj)
        return JobTypeSerializer(job_type_instances, many=True).data

    def get_roles(self, obj):
        role_instances = Role.objects.filter(Intersts=obj)
        return RoleSerializer(role_instances, many=True).data

    class Meta:
        model = Intersts
        fields = [
            'current_level_id',
            'job_types',
            'roles',
            'country_id',
            'search_status_id'
        ]
        read_only_fields = ['id']


class ExpirenceSerializer(serializers.ModelSerializer):
    expiernce_type_id = serializers.PrimaryKeyRelatedField(queryset=JobType.objects.all(), required=False,
                                                           source='JobType')
    job_role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=False, source='Role')
    career_level_id = serializers.PrimaryKeyRelatedField(queryset=CurrentLevel.objects.all(), required=False,
                                                         source='CurrentLevel')
    company_size_id = serializers.PrimaryKeyRelatedField(queryset=CompanySize.objects.all(), required=False,
                                                         source='CompanySize')
    company_industry_id = serializers.PrimaryKeyRelatedField(queryset=CompanyIndustry.objects.all(), required=False,
                                                             source='CompanyIndustry')

    class Meta:
        model = Expirence
        fields = [
            'expiernce_type_id',
            'job_role_id',
            'career_level_id',
            'company_size_id',
            'company_industry_id',
            'job_title',
            'company_name',
            'from_date',
            'is_work_there',
            'description',
            'career_level',
            'company_size',
            'company_industry',
            'starting_salary',
            'ending_salary'
        ]
        read_only_fields = ['id']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class JobSeekerProfileSerializer(serializers.ModelSerializer):
    general_infos = GeneralInfoSerializer(required=True)
    intersts = InterstsSerializer(required=True)
    skills = serializers.SerializerMethodField()
    expierences = serializers.SerializerMethodField()

    def get_skills(self, obj):
        skill_instances = Skill.objects.filter(JobSeekerProfile=obj)
        return SkillSerializer(skill_instances, many=True).data

    def get_expierences(self,obj):
        expierence_instances =  Expirence.objects.filter(JobSeekerProfile=obj)
        return ExpirenceSerializer(expierence_instances,many=True).data

    class Meta:
        model = JobSeekerProfile
        fields = ['general_infos','intersts','skills','expierences']
        read_only_fields = ['id']


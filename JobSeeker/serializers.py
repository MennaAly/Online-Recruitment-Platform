from django.contrib.auth.models import User
from rest_framework import serializers

# from Employer.models import CompanySize, CompanyIndustry
from Authentication.models import Profile
from Job.models import JobPost
from Job.serializers import JobPostMiniSerializer
from .models import JobSeekerProfile, GeneralInfo, Intersts, Expirence, Skill, CurrentLevel, JobType, Role, Country, \
    SearchStatus, YearsOfExpiernce, JobSeekerAndJobPosts
from MasterData.models import CompanySize, CompanyIndustry


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
                                                               source='years_of_expiernce', required=False)

    class Meta:
        model = Skill
        fields = ['skill_name', 'profiency_rate', 'interest_rate', 'years_of_expiernce_id']
        read_only_fields = ['id']


class InterstsSerializer(serializers.ModelSerializer):
    current_level_id = serializers.PrimaryKeyRelatedField(queryset=CurrentLevel.objects.all(), source='current_level',
                                                          required=False)
    job_types = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), source='country', required=False)
    search_status_id = serializers.PrimaryKeyRelatedField(queryset=SearchStatus.objects.all(), source='search_status',
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
                                                           source='expiernce_type')
    job_role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=False, source='job_role')
    career_level_id = serializers.PrimaryKeyRelatedField(queryset=CurrentLevel.objects.all(), required=False,
                                                         source='career_level')
    company_size_id = serializers.PrimaryKeyRelatedField(queryset=CompanySize.objects.all(), required=False,
                                                         source='company_size')
    company_industry_id = serializers.PrimaryKeyRelatedField(queryset=CompanyIndustry.objects.all(), required=False,
                                                             source='company_industry')

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
            'starting_salary',
            'ending_salary'
        ]
        read_only_fields = ['id']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class JobSeekerProfileSerializer(serializers.ModelSerializer):
    general_profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), required=False)
    # it will be sent as an object
    general_info = serializers.PrimaryKeyRelatedField(queryset=GeneralInfo.objects.all(), required=False)
    # it will be sent as an object
    intersts = serializers.PrimaryKeyRelatedField(queryset=Intersts.objects.all(), required=False)
    # it will be sent as ids
    skills = serializers.SerializerMethodField()
    # it will be sent as ids
    expierences = serializers.SerializerMethodField()

    def get_skills(self, obj):
        skill_instances = Skill.objects.filter(JobSeekerProfile=obj)
        return SkillSerializer(skill_instances, many=True).data

    def get_expierences(self, obj):
        expierence_instances = Expirence.objects.filter(JobSeekerProfile=obj)
        return ExpirenceSerializer(expierence_instances, many=True).data

    class Meta:
        model = JobSeekerProfile
        fields = ['general_profile', 'general_info', 'intersts', 'skills', 'expierences']
        read_only_fields = ['id']


class JobSeekerAndJobPostsSerializer(serializers.ModelSerializer):
    job_seeker_id = serializers.PrimaryKeyRelatedField(queryset=JobSeekerProfile.objects.all(), required=False,
                                                       source='job_seeker')
    job_post_id = serializers.PrimaryKeyRelatedField(queryset=JobPost.objects.all(), required=False, source='job_post')

    class Meta:
        model = JobSeekerAndJobPosts
        fields = [
            'id',
            'job_seeker_id',
            'job_post_id',
            'is_saved',
            'is_applied_for'
        ]
        read_only_fields = ['id']


class JobSeekerAndMiniJobPostsSerializer(serializers.ModelSerializer):
    job_post = JobPostMiniSerializer(read_only=True)

    class Meta:
        model = JobSeekerAndJobPosts
        fields = [
            'id',
            'job_post'
        ]
        read_only_fields = ['id']


class JobSeekerMiniSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        user = Profile.objects.filter(jobseekerprofile=obj)
        user_name = User.objects.filter(id=user)
        return user_name

    class Meta:
        model = JobSeekerProfile
        fields = [
            'id',
            'name'
        ]
        read_only_fields = ['id']

class MiniJobSeekerAndJobPostsSerializer(serializers.ModelSerializer):
    job_seeker = JobSeekerMiniSerializer(read_only=True)

    class Meta:
        model = JobSeekerAndJobPosts
        fields =[
            'id',
            'job_seeker'
        ]

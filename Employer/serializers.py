from rest_framework import serializers

from Authentication.models import Profile
from .models import EmployerProfile, ContactInfo
from MasterData.models import CompanySize, CompanyIndustry ,Role


class ContactInfoSerializer(serializers.ModelSerializer):
    job_role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(),required=False,source='job_role')
    class Meta:
        model = ContactInfo
        fields = ['username',
                  'title',
                  'job_role_id',
                  'mobile_number']
        read_only_fields = ['id']


class EmployerProfileSerializer(serializers.ModelSerializer):
    general_profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), required=False)
    contact_info_id = serializers.PrimaryKeyRelatedField(queryset=ContactInfo.objects.all(), required=False,
                                                         source='ContactInfo')
    # contact_info = ContactInfoSerializer(required=False)
    company_industry_id = serializers.PrimaryKeyRelatedField(queryset=CompanyIndustry.objects.all(), required=False,
                                                             source='company_industry')
    company_size_id = serializers.PrimaryKeyRelatedField(queryset=CompanySize.objects.all(), required=False,
                                                         source='company_size')

    class Meta:
        model = EmployerProfile
        fields = [
            'general_profile',
            'contact_info_id',
            'company_industry_id',
            'company_size_id',
            'company_name',
            'company_phone',
            'company_website'
        ]
        read_only_fields = ['id']

from rest_framework import serializers

from Authentication.models import Profile
from .models import EmployerProfile, ContactInfo
from MasterData.models import CompanySize, CompanyIndustry


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class EmployerProfileSerializer(serializers.ModelSerializer):
    general_profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), required=False)
    contact_info_id = serializers.PrimaryKeyRelatedField(queryset=ContactInfo.objects.all(), required=False,
                                                         source='ContactInfo')
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

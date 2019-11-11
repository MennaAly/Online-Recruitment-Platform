from rest_framework import serializers

from Authentication.models import Profile
from .models import EmployerProfile, ContactInfo
from MasterData.models import CompanySize, CompanyIndustry, Role , Country


class CompanyIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyIndustry
        fields = '__all__'


class CompanySizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySize
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    job_role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=False, source='job_role')

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

    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(),required=False,source='country')

    contact_info_object = serializers.SerializerMethodField()

    company_industry_object = serializers.SerializerMethodField()

    company_size_object = serializers.SerializerMethodField()

    def get_contact_info_object(self, obj):
        contact_info_object = ContactInfo.objects.filter(employerprofile=obj)
        return ContactInfoSerializer(contact_info_object, many=True).data

    def get_company_industry_object(self, obj):
        company_industry_object = CompanyIndustry.objects.filter(employerprofile=obj).first()
        return CompanyIndustrySerializer(company_industry_object).data

    def get_company_size_object(self, obj):
        company_size = CompanySize.objects.filter(employerprofile=obj).first()
        return CompanySizeSerializer(company_size).data

    class Meta:
        model = EmployerProfile
        fields = [
            'general_profile',
            'contact_info_id',
            'company_industry_id',
            'company_size_id',
            'company_name',
            'company_phone',
            'company_website',
            'contact_info_object',
            'company_industry_object',
            'company_size_object',
            'country_id'
        ]
        read_only_fields = ['id']

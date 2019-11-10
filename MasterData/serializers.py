from rest_framework import serializers
from .models import Role , CurrentLevel , JobType ,Language

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CurrentLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLevel
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

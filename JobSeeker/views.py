from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets , status
from rest_framework.response import Response
from .models import JobSeekerProfile
from .serializers import JobSeekerProfileSerializer, GeneralInfoSerializer, InterstsSerializer, SkillSerializer, \
    ExpirenceSerializer


# Create your views here.


class CreateJobSeekerProfile(viewsets.ModelViewSet):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    general_info = {}
    intersts = {}
    skills = []
    experiences = []
    job_seeker_profile_dict = {}

    def save_general_info(self):
        general_info_serializer = GeneralInfoSerializer(data=self.general_info)
        general_info_serializer.is_valid(raise_exception=True)
        general_info_object = general_info_serializer.save()
        self.job_seeker_profile_dict['general_info'] = general_info_object.id

    def save_intersts(self):
        intersts_serialzier = InterstsSerializer(data=self.intersts)
        intersts_serialzier.is_valid(raise_exception=True)
        intersts_object = intersts_serialzier.save()
        self.job_seeker_profile_dict['intersts'] = intersts_object.id

    def save_skills(self):
        skill_ids = []
        for skill in self.skills:
            skill_serializer = SkillSerializer(data=skill)
            skill_serializer.is_valid(raise_exception=True)
            skill_object = skill_serializer.save()
            skill_ids.append(skill_object.id)
        self.job_seeker_profile_dict['skills'] = skill_ids

    def save_expiernces(self):
        expiernces_ids = []
        for expiernce in self.experiences:
            expiernce_serializer = ExpirenceSerializer(data=expiernce)
            expiernce_serializer.is_valid(raise_exception=True)
            expiernce_object = expiernce_serializer.save()
            expiernces_ids.append(expiernce_object.id)
        self.job_seeker_profile_dict['expiernces'] = expiernces_ids

    def save_job_seeker_profile(self):
        job_seeker_profile_serializer = JobSeekerProfileSerializer(data=self.job_seeker_profile_dict)
        job_seeker_profile_serializer.is_valid(raise_exception=True)
        job_seeker_profile_serializer.save()

    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # get data
        self.general_info = request.data.get('general_info')
        self.intersts = request.data.get('intersts')
        self.skills = request.data.get('skills')
        self.experiences = request.data.get('experiences')
        # save user general info
        self.save_general_info()
        # save user intersts
        self.save_intersts()
        # save user skills
        self.save_skills()
        # save user experiences
        self.save_expiernces()
        #save job seeker profile
        self.save_job_seeker_profile()
        return Response(status=status.HTTP_201_CREATED)

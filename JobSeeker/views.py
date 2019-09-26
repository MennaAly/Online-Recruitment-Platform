from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import JobSeekerProfile, JobType, Role
from .serializers import JobSeekerProfileSerializer, GeneralInfoSerializer, InterstsSerializer, SkillSerializer, \
    ExpirenceSerializer


# Create your views here.


class UpdateJobSeekerProfile(generics.UpdateAPIView):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    general_info = {}
    intersts = {}
    intersts_jobtypes = []
    intersts_roles = []
    skills = []
    experiences = []
    job_seeker_profile_dict = {}

    def save_general_info(self):
        general_info_serializer = GeneralInfoSerializer(data=self.general_info)
        general_info_serializer.is_valid(raise_exception=True)
        return general_info_serializer.save()

    def save_intersts_jobtypes(self, interst_object):
        interst_jobtype_list = JobType.objects.filter(id__in=self.intersts_jobtypes)
        interst_object.job_type.add(*interst_jobtype_list)
        return interst_object

    def save_intersts_roles(self, interst_object):
        interst_roles_list = Role.objects.filter(id__in=self.intersts_roles)
        interst_object.role.add(*interst_roles_list)
        return interst_object

    def save_intersts(self):
        intersts_serialzier = InterstsSerializer(data=self.intersts)
        intersts_serialzier.is_valid(raise_exception=True)
        intersts_object = intersts_serialzier.save()
        intersts_object = self.save_intersts_jobtypes(intersts_object)
        intersts_object = self.save_intersts_roles(intersts_object)
        return intersts_object.save()

    def save_skills(self, job_seeker_profile_object):
        # can i replace the serializers with many=true ??
        for skill in self.skills:
            skill_serializer = SkillSerializer(data=skill)
            skill_serializer.is_valid(raise_exception=True)
            skill_object = skill_serializer.save()
            job_seeker_profile_object.skills.add(skill_object)
        return job_seeker_profile_object

    def save_expiernces(self, job_seeker_profile):
        for expiernce in self.experiences:
            expiernce_serializer = ExpirenceSerializer(data=expiernce)
            expiernce_serializer.is_valid(raise_exception=True)
            expiernce_object = expiernce_serializer.save()
            job_seeker_profile.experiences.add(expiernce_object)
        return job_seeker_profile

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        # get data
        self.general_info = request.data.get('general_info')
        self.intersts = request.data.get('intersts')
        self.intersts_jobtypes = request.data.get('intersts_jobtypes')
        self.intersts_roles = request.data.get('intersts_roles')
        self.skills = request.data.get('skills')
        self.experiences = request.data.get('experiences')
        # filter and get the profile object from the data base
        jobseeker_profile_object = JobSeekerProfile.objects.filter(pk=request.data.get('profile_id')).first()
        # save user general info
        general_info_obj = self.save_general_info()
        # save user intersts
        intersts_obj = self.save_intersts()
        # save user skills
        self.save_skills(jobseeker_profile_object)
        # save user experiences
        self.save_expiernces(jobseeker_profile_object)
        # save job seeker profile
        JobSeekerProfile.objects.filter(pk=request.data.get('profile_id')).update(general_info=general_info_obj, intersts=intersts_obj)
        return Response(status=status.HTTP_201_CREATED)

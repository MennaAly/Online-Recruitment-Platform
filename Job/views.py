from django.db import transaction
from rest_framework import viewsets , status , generics
from MasterData.models import Role , Language
from .models import  JobPost
from .serializers import PointSerializer, ParagraphSerializer ,JobPostSerializer
from JobSeeker.models import JobSeekerProfile
from rest_framework.response import Response


# Create your views here.

class PostJob(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    job_description_paragraphs = []
    job_roles_ids = []
    languages_ids = []
    job_description = {}
    post_job_dict = {}

    def save_paragraph_points(self, paragraph, points):
        for point in points:
            point_serializer = PointSerializer(data=point)
            point_serializer.is_valid(raise_exception=True)
            point_instance = point_serializer.save()
            paragraph.points.add(point_instance)
        paragraph.save()
        return paragraph

    def save_job_description(self,job_post_instance):
        for paragraph in self.job_description_paragraphs:
            paragraph_serializer = ParagraphSerializer(data=paragraph)
            paragraph_serializer.is_valid(raise_exception=True)
            paragraph_instance = paragraph_serializer.save()
            paragraph_instance = self.save_paragraph_points(paragraph=paragraph_instance, points=paragraph['_points'])
            job_post_instance.pargraphs.add(paragraph_instance)
        job_post_instance.save()
        return job_post_instance.id

    def save_job_roles(self,job_post_instance):
        job_role_instances = Role.objects.filter(id__in=self.job_roles_ids)
        job_post_instance.job_roles.add(*job_role_instances)
        job_post_instance.save()

    def save_languages(self,job_post_instance):
        language_instances = Language.objects.filter(id__in=self.languages_ids)
        job_post_instance.languages.add(*language_instances)
        job_post_instance.save()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        self.post_job_dict = request.data
        self.job_description_paragraphs = self.post_job_dict['job_description_paragraphs']
        self.job_roles_ids = self.post_job_dict['job_roles_ids']
        self.languages_ids = self.post_job_dict['languages_ids']
        job_post_serializer = JobPostSerializer(data=self.post_job_dict)
        job_post_serializer.is_valid(raise_exception=True)
        job_post_instance = job_post_serializer.save()
        self.save_job_description(job_post_instance)
        self.save_job_roles(job_post_instance)
        self.save_languages(job_post_instance)
        return Response(status=status.HTTP_201_CREATED)


class ApplyForJob(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        job_seeker_id = request.data.get('job_seeker_id')
        job_id = request.data.get("job_id")
        job = JobPost.objects.filter(id=job_id).first()
        job_seeker = JobSeekerProfile.objects.filter(id=job_seeker_id).first()
        job.applicants.add(job_seeker)
        job.save()
        return Response(status=status.HTTP_200_OK)
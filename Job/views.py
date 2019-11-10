from django.db import transaction
from django.db.models import Q
from rest_framework import viewsets, status, generics, filters

from JobSeeker.serializers import JobSeekerAndJobPostsSerializer, JobSeekerAndMiniJobPostsSerializer, \
    MiniJobSeekerAndJobPostsSerializer
from MasterData.models import Role, Language
from .models import JobPost
from .serializers import PointSerializer, ParagraphSerializer, JobPostSerializer
from JobSeeker.models import JobSeekerProfile, JobSeekerAndJobPosts
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


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

    def save_job_description(self, job_post_instance):
        for paragraph in self.job_description_paragraphs:
            paragraph_serializer = ParagraphSerializer(data=paragraph)
            paragraph_serializer.is_valid(raise_exception=True)
            paragraph_instance = paragraph_serializer.save()
            paragraph_instance = self.save_paragraph_points(paragraph=paragraph_instance, points=paragraph['_points'])
            job_post_instance.pargraphs.add(paragraph_instance)
        job_post_instance.save()
        return job_post_instance.id

    def save_job_roles(self, job_post_instance):
        job_role_instances = Role.objects.filter(id__in=self.job_roles_ids)
        job_post_instance.job_roles.add(*job_role_instances)
        job_post_instance.save()

    def save_languages(self, job_post_instance):
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


class JobPostFilter(FilterSet):
    # print('heereeee')
    class Meta:
        model = JobPost
        fields = {
            # 'company__id':['exact',],
            'is_active': ['exact', ],
            # 'career_level__id' : ['exact',],
            # 'job_type__id' : ('exact',)
        }


# when you use filter class in your view set you will need to make a modelviewset
class filterJobs(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = JobPostFilter

    # def retrieve(self, request, *args, **kwargs):
    #     employer_id = request.data.get('employer_id')
    #     level_id = request.data.get('level_id')
    #     job_type_id = request.data.get('job_type_id')
    #     #how to filter MM relation
    #     role_ids = request.data.get('role_id')
    #     job_posts = JobPost.objects.filter(Q(company__id=employer_id) | Q(career_level__id=level_id)|
    #                                        Q(job_type__id=job_type_id) | Q(job_roles__id__in=role_ids),is_active=True)
    #     # to use the serializer to (read data) you will use Serializer(object,many=True).data
    #     # to use the serializer to (write data) you will use Serialzier(data=) then you validate the data
    #     # and save it
    #     return Response(JobPostSerializer(job_posts, many=True).data, status=status.HTTP_200_OK)

class JobSeekerAndJobsFilter(FilterSet):
    class Meta:
        model = JobSeekerAndJobPosts
        fields = {
            'job_seeker__id' : ['exact',],
            'job_post__id' : ['exact',],
            'is_saved' : ['exact',],
            'is_applied_for' : ['exact',]
        }

class JobSeekerAndJobs(viewsets.ModelViewSet):
    queryset = JobSeekerAndJobPosts.objects.all()
    serializer_class = JobSeekerAndJobPostsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = JobSeekerAndJobsFilter

    def get_serializer_class(self):
        serializer_name = self.request.query_params.get('serializer_name')
        if serializer_name == 'mini_job_posts':
            return JobSeekerAndMiniJobPostsSerializer
        elif serializer_name == 'mini_job_seekers':
            return MiniJobSeekerAndJobPostsSerializer
        return JobSeekerAndJobPostsSerializer
    """
    apply for a job 
    save job
    get all saved jobs for required jobseeker
    get all applied jobs for required jobseeker
    get all applied jobs for required company and required job seeker
    """
    # def create(self, request, *args, **kwargs):
    #     # data =
    #     print(request.data)
    #     jobseeker_and_jobposts_serializer = JobSeekerAndJobPostsSerializer(data=request.data)
    #     print('heeeeeeeeeeeeereeeeeeeeeeee',jobseeker_and_jobposts_serializer)
    #     jobseeker_and_jobposts_serializer.is_valid(raise_exception=True)
    #     jobseeker_and_jobposts_serializer.save()
    #     return Response(status=status.HTTP_200_OK)




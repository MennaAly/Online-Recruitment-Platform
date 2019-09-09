# standrds
# core django
from django.db import transaction
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
# third library
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
# your app
from .serializers import GeneralProfileSerializer
from Employer.models import EmployerProfile
from Employer.serializers import EmployerProfileSerializer
from JobSeeker.models import JobSeekerProfile
from JobSeeker.serializers import JobSeekerProfileSerializer


class Login(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Register(viewsets.ModelViewSet):
    user_model = get_user_model()
    queryset = User.objects.all()
    profile_type = ''
    profile_dict = {}

    def get_serializer_class(self):
        if self.profile_type == 'employer_profile':
            return EmployerProfileSerializer
        elif self.profile_type == 'jobseeker_profile':
            return JobSeekerProfileSerializer

    def save_profile(self):
        profile_serializer = self.get_serializer(data=self.profile_dict)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

    def save_user(self, username, email, password):
        user = self.user_model.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        self.profile_type = request.data.get('profile_type')
        user = self.save_user(username,email,password)
        # when sending data to serializer in foreign key you need to send the id , but when you create object you can
        # use either the foreign key object itself or the id
        self.profile_dict = {
            'general_profile': user.profile.id
        }
        self.save_profile()
        return Response(status=status.HTTP_201_CREATED)

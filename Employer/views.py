from rest_framework import status, generics
from rest_framework.response import Response
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer


# Create your views here.

class UpdateEmployerProfile(generics.UpdateAPIView):
    queryset = EmployerProfile.objects.all()

    def update(self, request, *args, **kwargs):
        employer_profile_serializer = EmployerProfileSerializer(data=request.data)
        employer_profile_serializer.is_valid(raise_exception=True)
        employer_profile_serializer.save()
        return Response(status=status.HTTP_200_OK)

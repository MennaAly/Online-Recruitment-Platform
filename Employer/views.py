from django.db import transaction
from rest_framework import status, generics
from rest_framework.response import Response
from .models import EmployerProfile, ContactInfo
from .serializers import EmployerProfileSerializer, ContactInfoSerializer


# Create your views here.

class UpdateEmployerProfile(generics.UpdateAPIView):
    queryset = EmployerProfile.objects.all()

    def saveContractInfo(self, request):
        contact_info_serialzier = ContactInfoSerializer(data=request.data.get('contact_info_object'))
        contact_info_serialzier.is_valid(raise_exception=True)
        return contact_info_serialzier.save().id

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        employer_profile_instance = EmployerProfile.objects.filter(id=request.data.get("id")).first()
        contact_info_id = self.saveContractInfo(request)
        employer_profile_dict = request.data
        employer_profile_dict['contact_info_id'] = contact_info_id
        """
        if u want the serializer to update the instance 
        serializer(old instance, data=data) => here it will be in the update mode
        serializer(data=data) => creation mode
        """
        employer_profile_serializer = EmployerProfileSerializer(employer_profile_instance, data=employer_profile_dict)
        employer_profile_serializer.is_valid(raise_exception=True)
        employer_profile_serializer.save()
        return Response(status=status.HTTP_200_OK)

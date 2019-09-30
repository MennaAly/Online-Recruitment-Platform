from django.test import TestCase , Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from Authentication.models import Profile
from django.contrib.auth.models import User
from .models import EmployerProfile

# Create your tests here.
class EmployerTest(TestCase):
    def SetUp(self):
        self.client = Client()
        self.edit_url = reverse('/update_employer_profile/')
        self.user = User.objects.create(username='Menna',email='menna@gmail.com',password='1234')
        self.general_profile = Profile.objects.create(user=self.user)
        self.employer_profile = EmployerProfile.objects.create(general_profile=self.general_profile)

    def test_employer_profile_POST_edit_profile(self):
        response = self.client.post(reverse(self.edit_url),{
            'profile_id' :  self.employer_profile.id,
            'general_profile_id' : self.general_profile.id,
            'company_name' : 'Smart',
            'company_phone' : '0114115510',
            'company_website' : 'mennaali@gmail.com',
            'company_industry' : 1,
            'company_size' : 1
        })
        self.assertEqual(response.status_code,200)
        self.assertEqual(EmployerProfile.objects.first().company_name,'Smart')

    def test_employer_profile_fails_blank(self):
        response = self.client.post(reverse(self.edit_url),{})
        self.assertEqual(response.status_code,500)


    def test_employer_profile_fails_invalid(self):
        response = self.client.post(reverse(self.edit_url),{
            'profile_id': self.employer_profile.id,
            'general_profile_id' : self.general_profile.id,
            'company_name' : 'Smart',
            'company_phone' : '0114115510',
            'company_website' : 'mennaali@gmail.com',
            'company_industry' : 300,
            'company_size' : 1
        })
        self.assertRaises(ObjectDoesNotExist)
        self.assertEqual(response.status_code,500)

    def test_employer_profile_fails_inavlid_profile(self):
        response = self.client.post(reverse(self.edit_url), {
            'profile_id': 50,
            'general_profile_id': self.general_profile.id,
            'company_name': 'Smart',
            'company_phone': '0114115510',
            'company_website': 'mennaali@gmail.com',
            'company_industry': 300,
            'company_size': 1
        })
        self.assertRaises(ObjectDoesNotExist)
        self.assertEqual(response.status_code, 500)

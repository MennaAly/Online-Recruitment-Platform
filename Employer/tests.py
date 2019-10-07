from django.test import TestCase , Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from Authentication.models import Profile
from django.contrib.auth.models import User
from .models import EmployerProfile

# Create your tests here.
class EmployerTest(TestCase):
    """
    use setUpTestData for the shared data and setUp for the per-test-method client
    """
    @classmethod
    def setUpTestData(cls):
        cls.edit_url = reverse('/update_employer_profile/')
        cls.user = User.objects.create(username='Menna', email='menna@gmail.com', password='1234')
        cls.general_profile = Profile.objects.create(user=cls.user)
        cls.employer_profile = EmployerProfile.objects.create(general_profile=cls.general_profile)

    def SetUp(self):
        self.client = Client()

    def test_employer_profile_PUT_edit_profile(self):
        response = self.client.put(self.edit_url,{
            'id' :  self.employer_profile.id,
            "contact_info_object": {
                "username": "Youmna Ali",
                "title": "Translater",
                "job_role_id": 21,
                "mobile_number": "01141155710"
            },
            'company_name' : 'Smart',
            'company_phone' : '0114115510',
            'company_website' : 'mennaali@gmail.com',
            'company_industry' : 1,
            'company_size' : 1
        })
        self.assertEqual(response.status_code,200)
        self.assertEqual(EmployerProfile.objects.first().company_name,'Smart')

    def test_employer_profile_fails_blank(self):
        response = self.client.put(self.edit_url,{})
        self.assertEqual(response.status_code,500)


    def test_employer_profile_fails_invalid(self):
        response = self.client.put(self.edit_url,{
            'profile_id': self.employer_profile.id,
            "contact_info_object": {
                "username": "Youmna Ali",
                "title": "Translater",
                "job_role_id": 21,
                "mobile_number": "01141155710"
            },
            'company_name' : 'Smart',
            'company_phone' : '0114115510',
            'company_website' : 'mennaali@gmail.com',
            'company_industry' : 300,
            'company_size' : 1
        })
        self.assertRaises(ObjectDoesNotExist)
        self.assertEqual(response.status_code,500)

    def test_employer_profile_fails_inavlid_profile(self):
        response = self.client.put(self.edit_url, {
            'profile_id': 50,
             "contact_info_object": {
                "username": "Youmna Ali",
                "title": "Translater",
                "job_role_id": 21,
                "mobile_number": "01141155710"
            },
            'company_name': 'Smart',
            'company_phone': '0114115510',
            'company_website': 'mennaali@gmail.com',
            'company_industry': 300,
            'company_size': 1
        })
        self.assertRaises(ObjectDoesNotExist)
        self.assertEqual(response.status_code, 500)

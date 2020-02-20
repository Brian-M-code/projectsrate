from django.test import TestCase
from .models import Profile,Projects,Rates


class ProfileTestClass(TestCase):
    def setUp(self):
        self.brian = Profile(profile_photo='def.jpg',bio='I boss everything I do.', phone_number='070123456')

    def test_instance(self):
        self.assertTrue(isinstance(self.brian,Profile))

    def test_save(self):
        self.brian.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)


class RateTestClass(TestCase):
    def setUp(self):
        
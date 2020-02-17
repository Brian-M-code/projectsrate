from django.test import TestCase

from .models import Projects,Profile

# Create your tests here.
# Create your tests here.Projects
class Projects(TestCase):

    #set up method
    def setUp(self):
        self.description= Projects(location='description')

    def test_instance(self):
        self.assertTrue(isinstance(self.description,Projects))

    def tearDown(self):
        Projects.objects.all().delete()

    def test_save_method(self):
        self.description.save_location()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.description.delete_location('description')
        projects = Projects.objects.all()
        self.assertTrue(len(projects)==0)
from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.

# Set up method
class CategoryTestClass(TestCase):

  def setUp(self):
    self.travel= Category(title = 'isiolo')

  
  def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))

# Set up method
class LocationTestClass(TestCase):

  def setUp(self):
    self.nairobi = Location(title = 'town')
  
  def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))  


# Set up method 
# class ImageTestClass(TestCase):

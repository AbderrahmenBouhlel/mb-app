from django.test import TestCase
from django.urls import reverse

from .models import Post
# Create your tests here.



class PostModelTest(TestCase):
    
    def setUp(self):   #to create a new database
        Post.objects.create(text='just a test')
        
    def test_text_content(self):
        post = Post.objects.get(id=1)
        except_object_name = f'{post.text}'
        self.assertEqual(except_object_name,'just a test')
        
        
class HomePageviewTest(TestCase):
    def setUp(self): # create a simple database and to it a row
        Post.objects.create(text='this is another test')
        
    # Test whether the view is accessible at the expected UR
    def test_view_url_exists_at_proper_location(self):
        # Send a GET request to the root URL '/'
        resp = self.client.get('/')
        # Assert that the HTTP response status code is 200 (OK)
        self.assertEqual(resp.status_code,200)
        
        
    # Test whether the view is accessible by using its name
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        
    # Test whether the correct template is used by the view
    def test_view_uses_correct_templates(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        
        # Assert that the response used the 'home.html' template
        self.assertTemplateUsed(resp,'home.html')
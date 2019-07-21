from django.test import TestCase
from .models import Feature


class FeatureTest(TestCase):
    """
    List of tests to be run against
    the Features model
    """
    def test_str(self):
        test_name = Feature(name='New Feature')
        self.assertEqual(str(test_name), 'New Feature')
    

   

    
        
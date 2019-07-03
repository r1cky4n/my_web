"""TODO: write some tests..."""
from django.test import TestCase

class HelloWorldTestCase(TestCase):
    """Sanity Test Case."""
    def test_hello_world(self):
        """Sanity Check"""
        self.assertEqual(1, 1)

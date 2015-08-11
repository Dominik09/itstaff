from django.test import TestCase, Client
from sheet.models import Sheet

class TestNews(TestCase):
	def test_addnews(self):
		response=self.client.get('/addnews/')
		self.assertEqual(response.resolver_match.func.__name__, 'addnews')
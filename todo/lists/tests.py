from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# when we go to url '/' 200 code is sent back

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')

		self.assertEqual(found.func, home_page)

# Create your tests here.




# 1. user story

# 2. expected fail

# 3. write minimum code needed for test(s) to pass
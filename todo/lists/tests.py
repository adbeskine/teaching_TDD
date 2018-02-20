from django.test import TestCase
from django.urls import resolve, reverse
from lists.views import home_page


class HomePageTest(TestCase):
	# when we go to url '/' 200 code is sent back
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')

		self.assertEqual(found.func, home_page)


	# Когда user переходит по url ('/') то отобразить HttpResponse
	def test_when_user_go_to_root_url(self):
		response = self.client.get(reverse('home_page'))

		get_html = response.content.decode('utf8')

		self.assertIn('Hello World', get_html)





# 1. user story

# 2. expected fail

# 3. write minimum code needed for test(s) to pass
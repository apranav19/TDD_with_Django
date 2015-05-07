from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        # Send a POST request with the following piece of information
        request.POST['item_text'] = 'A new item'

        response = home_page(request)
        # Check if response contains this new item
        self.assertIn('A new item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new item'}
        )
        self.assertEqual(response.content.decode(), expected_html)

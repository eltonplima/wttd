# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('core:home'))

    def test_get(self):
        """
        GET / must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')
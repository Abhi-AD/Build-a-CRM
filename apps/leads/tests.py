from django.test import TestCase
from django.shortcuts import reverse


class IndexPageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse("leads:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

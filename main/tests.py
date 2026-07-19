from django.test import TestCase
from django.urls import reverse

class Test(TestCase):
    def testh(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def testr(self):
        response = self.client.get(reverse("reviews"))
        self.assertEqual(response.status_code, 200)

    def testurl(self):
        self.assertEqual(reverse("home"), "/")
        self.assertEqual(reverse("reviews"), "/reviews/")
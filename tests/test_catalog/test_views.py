import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse


class TestIndexAPIView(TestCase):
    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_index_get(self):
        pass


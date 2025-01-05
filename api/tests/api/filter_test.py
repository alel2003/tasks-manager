from django.urls import reverse
from rest_framework import status

from api.tests.api.test_api import TestAPI


class TestFilteredTask(TestAPI):
    def setUp(self):
        super().setUp()

    def filter_by_status(self):
        response = self.client.get("/api/task-filter/", {"status": "done"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["status"], "done")

    def filter_by_title(self):
        response = self.client.get("/api/task-filter/", {"title": "base task api"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["title"], "base task api")

    def filter_by_date_end(self):
        response = self.client.get(
            "/api/task-filter/", {"date_end": self.save_date_end_str}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["date_end"], self.save_date_end_str)

    def test_filter_by_user(self):
        response = self.client.get("/api/task-filter/", {"user": self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["user"], self.user.id)

    def test_multiple_filters(self):
        response = self.client.get(
            "/api/task-filter/", {"status": "done", "title": "base task api"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["title"], "base task api")

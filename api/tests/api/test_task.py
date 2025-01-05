from django.urls import reverse
from rest_framework import status

from api.tests.api.test_api import TestAPI


class TestApiTask(TestAPI):
    def test_get_tasks(self):
        url = reverse("tasks")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_get_task_details(self):
        url = reverse("task-details", args=[self.base_task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = reverse("task-create")
        response = self.client.post(url, self.json_create_task, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["title"], self.json_create_task["title"])

    def test_update_task(self):
        url = reverse("task-update", args=[self.base_task.id])
        response = self.client.patch(url, self.json_update_task, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], self.json_update_task["status"])

    def test_delete_task(self):
        url = reverse("task-delete", args=[self.base_task.id])
        response = self.client.patch(url, self.json_delete_task, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["delete"], self.json_delete_task["delete"])

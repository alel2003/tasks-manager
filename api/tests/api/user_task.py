from datetime import datetime, timezone

from django.urls import reverse
from rest_framework import status

from api.models import Task
from api.tests.api.test_api import TestAPI


class CreateUserTask(TestAPI):
    def setUp(self):
        super().setUp()

        self.base_task_data = Task.objects.create(
            title="base task api",
            description="base task api description",
            user=self.user,
            date_end=self.save_date_end,
        )
        self.json_user_data = {"username": "testuser", "password": "testuser"}

        self.json_transfer_user_data = {
            "pk": self.base_task_data.pk,
            "user_id": self.user.pk,
        }

    def test_create_user(self):
        url = reverse("create-user")
        response = self.client.post(url, self.json_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.data)
        self.assertEqual(response.data["username"], self.json_user_data["username"])

    def test_transfer_user(self):
        url = reverse("task-transfer", kwargs=self.json_transfer_user_data)
        response = self.client.patch(url, {"user": self.user.pk}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.pk)

from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from api.models import Task


class TestSetup(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")

        self.save_date_end = datetime(2025, 1, 3, 12, 0, tzinfo=timezone.utc)
        self.save_date_end_str = self.save_date_end.isoformat()

        self.base_task = Task.objects.create(
            title="base task test title",
            description="base task test description",
            user=self.user,
            date_end=self.save_date_end,
        )

        self.base_tasks = [
            {
                "title": "task 1",
                "description": "task test description 1",
                "user": self.user,
                "date_end": self.save_date_end,
            },
            {
                "title": "task 2",
                "description": "task test description 2",
                "user": self.user,
                "date_end": self.save_date_end,
            },
            {
                "title": "task 3",
                "description": "task test description 3",
                "user": self.user,
                "date_end": self.save_date_end,
            },
        ]

        self.tasks = []
        for task_data in self.base_tasks:
            task = Task.objects.create(**task_data)
            self.tasks.append(task)

        self.number_tasks = 4

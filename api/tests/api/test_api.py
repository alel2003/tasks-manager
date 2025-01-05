from datetime import datetime, timezone

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Task


class TestAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuserapi", password="password"
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {str(refresh.access_token)}")

        self.save_date_end = datetime(2026, 1, 3, 12, 0, tzinfo=timezone.utc)
        self.save_date_end_str = self.save_date_end.isoformat()

        self.base_task = Task.objects.create(
            title="base task api",
            description="base task api description",
            status="done",
            user=self.user,
            date_end=self.save_date_end,
        )

        self.json_create_task = {
            "title": "base task api",
            "description": "base task api description",
            "user": self.user.id,
            "date_end": self.save_date_end,
        }

        self.json_update_task = {"status": "in_progress"}

        self.json_delete_task = {"delete": True}

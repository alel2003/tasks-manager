from datetime import datetime, timezone

from api.models import Task
from api.tests.test_setup import TestSetup


class TestModelTask(TestSetup):
    def test_create_task(self):
        self.task_new_data = Task.objects.create(
            title="new task test title",
            description="new task test description",
            user=self.user,
            date_end=self.save_date_end,
        )

    def test_task_data_str(self):
        self.assertEqual(
            str(self.base_task), f"BASE TASK TEST TITLE {self.base_task.date}"
        )

    def test_get_tasks(self):
        get_to_tasks = Task.objects.all()
        self.assertEqual(len(get_to_tasks), self.number_tasks)

    def test_get_task(self):
        get_to_task = Task.objects.get(pk=self.base_task.pk)
        self.assertEqual(get_to_task, self.base_task)

    def test_update_task(self):
        update_to_task = Task.objects.get(pk=self.base_task.pk)
        update_to_task.status = "in_progress"
        update_to_task.save()
        self.assertEqual(update_to_task.status, "in_progress")

    def test_delete_task(self):
        delete_to_task = Task.objects.get(pk=self.base_task.pk)
        delete_to_task.delete = True
        delete_to_task.save()
        self.assertEqual(delete_to_task.delete, True)

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = "new"
        IN_PROGRESS = "in_progress"
        DONE = "done"

    title = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title.upper()} {self.date}"

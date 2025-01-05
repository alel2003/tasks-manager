from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filter import TaskFilter
from .models import Task
from .serializers import (
    CreateTaskSerializer,
    CreateUserSerializer,
    TaskSerializer,
    TransferTaskSerializer,
)


class AuthRequiredMixin:
    permission_classes = [IsAuthenticated]


class BaseTaskData:
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ListTask(BaseTaskData, generics.ListAPIView):
    pass


class TaskDetails(BaseTaskData, AuthRequiredMixin, generics.RetrieveAPIView):
    pass


class CreateTask(AuthRequiredMixin, generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer


class UpdateTaskDetails(BaseTaskData, AuthRequiredMixin, generics.UpdateAPIView):
    pass


class DeleteTaskDetails(BaseTaskData, AuthRequiredMixin, generics.UpdateAPIView):
    pass


class FilterTasks(BaseTaskData, AuthRequiredMixin, generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter


class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class TransferTask(AuthRequiredMixin, generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TransferTaskSerializer

    def get_queryset(self):
        """Limit the tasks that a user can delegate."""
        return Task.objects.filter(user=self.request.user)

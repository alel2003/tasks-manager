from django.urls import path

from .views import (
    CreateTask,
    CreateUser,
    DeleteTaskDetails,
    FilterTasks,
    ListTask,
    TaskDetails,
    TransferTask,
    UpdateTaskDetails,
)

urlpatterns = [
    path("tasks/", ListTask.as_view(), name="tasks"),
    path("task-details/<int:pk>/", TaskDetails.as_view(), name="task-details"),
    path("task-create/", CreateTask.as_view(), name="task-create"),
    path("task-update/<int:pk>/", UpdateTaskDetails.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", DeleteTaskDetails.as_view(), name="task-delete"),
    path("task-filter/", FilterTasks.as_view(), name="task-filter"),
    path("create-user/", CreateUser.as_view(), name="create-user"),
    path(
        "task/<int:pk>/transfer/<int:user_id>/",
        TransferTask.as_view(),
        name="task-transfer",
    ),
]

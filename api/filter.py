from django_filters import rest_framework as filters

from .models import Task


class TaskFilter(filters.FilterSet):
    date_end = filters.DateFromToRangeFilter()
    title = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Task
        fields = ["status", "user", "date_end", "title"]

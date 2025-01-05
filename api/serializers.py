from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "user",
            "date",
            "date_end",
            "delete",
        ]


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "date_end"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return Task.objects.create(**validated_data)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class TransferTaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )

    class Meta:
        model = Task
        fields = ["user", "id"]

    def update(self, instance, validated_data):
        """Pass the task to a new user."""
        instance.user = validated_data.get("user")
        instance.save()
        return instance

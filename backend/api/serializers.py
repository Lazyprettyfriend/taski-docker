"""Сериализаторы для преобразования экземпляров моделей в JSON и обратно."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Task."""

    class Meta:
        """Метапараметры сериализатора TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')

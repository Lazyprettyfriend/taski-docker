"""Настройка панели администратора для приложения API."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройка модели Task в админ-панели."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)

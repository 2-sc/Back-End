from django.db import models
from django.utils import timezone


# from datetime import datetime


# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=20, verbose_name="todo")
    complete = models.BooleanField()
    register = models.DateField(verbose_name="today", default=timezone.now)

    def __str__(self):
        return self.todo


class Schedule(models.Model):
    schedule = models.CharField(max_length=20, verbose_name="schedule")
    register = models.DateField(verbose_name="today", default=timezone.now)

    def __str__(self):
        return self.schedule

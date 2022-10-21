from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    user_id = models.ForeignKey('user.User', verbose_name="user_id", on_delete=models.CASCADE, null=True)
    todo = models.CharField(max_length=20, verbose_name="todo")
    complete = models.BooleanField(default=False, verbose_name="complete")
    register = models.DateField(verbose_name="today", default=timezone.now)

    def __str__(self):
        return self.todo


class Schedule(models.Model):
    user_id = models.ForeignKey('user.User', verbose_name="user_id", on_delete=models.CASCADE, null=True)
    schedule = models.CharField(max_length=20, verbose_name="schedule")
    register = models.DateField(verbose_name="today", default=timezone.now)

    def __str__(self):
        return self.schedule


class Comment(models.Model):
    user_id = models.ForeignKey('user.User', verbose_name="user_id", on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=20, verbose_name="comment")
    register = models.DateField(verbose_name="today", default=timezone.now)

    def __str__(self):
        return self.comment

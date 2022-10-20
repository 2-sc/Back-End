from tabnanny import verbose
from django.db import models

# Create your models here.

class StopWatch(models.Model):
    email_id = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='email_id_s')
    subject = models.CharField(max_length=32)
    startTime = models.CharField(max_length=32)
    endTime = models.CharField(max_length=32)
    totalTime = models.CharField(max_length=32)
    register_dttm = models.CharField(max_length=32)

    class Meta:
        verbose_name = '스탑워치'
        verbose_name_plural = '스탑워치'
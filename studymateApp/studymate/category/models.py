from django.db import models
# Create your models here.

class Category(models.Model):
    email = models.EmailField(verbose_name='이메일')
    subject = models.CharField(max_length=64, verbose_name='과목')

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'
# Generated by Django 4.1.2 on 2022-10-10 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_alter_todo_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='register',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 10, 10, 8, 4, 58, 152176), verbose_name='today'),
        ),
    ]
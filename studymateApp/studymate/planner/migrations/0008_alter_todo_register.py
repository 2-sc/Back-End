# Generated by Django 4.1.2 on 2022-10-10 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_alter_todo_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='register',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 7, 0, 52, 910666), verbose_name='today'),
        ),
    ]

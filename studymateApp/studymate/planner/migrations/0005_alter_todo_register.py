# Generated by Django 4.1.2 on 2022-10-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_alter_todo_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='register',
            field=models.DateTimeField(blank=True, verbose_name='today'),
        ),
    ]

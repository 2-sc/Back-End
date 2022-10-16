# Generated by Django 3.2 on 2022-10-14 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StopWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=32)),
                ('startTime', models.CharField(max_length=32)),
                ('endTime', models.CharField(max_length=32)),
                ('totalTime', models.CharField(max_length=32)),
                ('register_dttm', models.CharField(max_length=32)),
                ('email_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_id_s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '스탑워치',
                'verbose_name_plural': '스탑워치',
            },
        ),
    ]
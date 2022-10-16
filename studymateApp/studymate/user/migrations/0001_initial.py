# Generated by Django 3.2 on 2022-10-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=20, verbose_name='닉네임')),
                ('image', models.ImageField(default='default.jpeg', upload_to='profile/', verbose_name='이미지')),
                ('info', models.TextField(verbose_name='자기소개')),
                ('d_day', models.DateField(verbose_name='디데이')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
            },
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-06 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-15 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200413_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpost',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]

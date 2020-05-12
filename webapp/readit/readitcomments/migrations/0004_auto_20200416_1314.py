# Generated by Django 3.0.4 on 2020-04-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200415_1348'),
        ('readitcomments', '0003_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='replys',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_replys', to='readitcomments.Comment'),
        ),
    ]

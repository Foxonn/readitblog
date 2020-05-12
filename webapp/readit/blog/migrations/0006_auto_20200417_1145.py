# Generated by Django 3.0.4 on 2020-04-17 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readitcomments', '0007_remove_comment_post'),
        ('blog', '0005_auto_20200417_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpost',
            name='comments',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='readitcomments.Comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='readitcomments.Comment'),
        ),
    ]

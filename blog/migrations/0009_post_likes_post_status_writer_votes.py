# Generated by Django 4.2.16 on 2024-12-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_writer_all_posts_writer_tokens_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default='no_status', max_length=15),
        ),
        migrations.AddField(
            model_name='writer',
            name='votes',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

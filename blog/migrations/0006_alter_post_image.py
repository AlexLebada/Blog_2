# Generated by Django 4.2.16 on 2024-12-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_uploadedfile_tokens_total_uploadedfile_tokens_useful_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', null=True, upload_to='img'),
        ),
    ]

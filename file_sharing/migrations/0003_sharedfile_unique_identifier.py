# Generated by Django 4.2.5 on 2023-10-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_sharing', '0002_remove_sharedfile_unique_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedfile',
            name='unique_identifier',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]

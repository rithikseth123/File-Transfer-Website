# Generated by Django 4.2.5 on 2023-10-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_sharing', '0005_alter_sharedfile_unique_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedfile',
            name='unique_identifier',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
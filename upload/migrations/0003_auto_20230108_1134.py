# Generated by Django 3.2.16 on 2023-01-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_dataqualitycheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataqualitycheck',
            name='integer_check',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='dataqualitycheck',
            name='string_check',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

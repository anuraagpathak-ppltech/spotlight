# Generated by Django 3.2.16 on 2023-01-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_auto_20230112_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]

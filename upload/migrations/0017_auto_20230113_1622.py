# Generated by Django 3.2.16 on 2023-01-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0016_auto_20230113_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source', models.CharField(blank=True, max_length=100, null=True)),
                ('table_records', models.IntegerField(blank=True, null=True)),
                ('total_records', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

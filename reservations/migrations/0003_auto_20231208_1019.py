# Generated by Django 3.2.23 on 2023-12-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20231207_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 3.2.23 on 2023-12-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='responded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
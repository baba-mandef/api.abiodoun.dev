# Generated by Django 3.2 on 2023-09-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20230908_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

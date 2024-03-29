# Generated by Django 3.2 on 2023-08-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender_name', models.CharField(max_length=150)),
                ('sender_email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

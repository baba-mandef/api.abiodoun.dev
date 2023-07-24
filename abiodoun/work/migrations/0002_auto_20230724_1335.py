# Generated by Django 3.2 on 2023-07-24 13:35

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='description',
            field=models.CharField(default='description', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='en_body',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AddField(
            model_name='work',
            name='en_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.CharField(default='link', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='repo',
            field=models.CharField(default='repo', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='stack',
            field=models.CharField(default='stack', max_length=255),
            preserve_default=False,
        ),
    ]

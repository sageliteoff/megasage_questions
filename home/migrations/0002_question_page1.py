# Generated by Django 2.0.7 on 2019-01-21 18:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='page1',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1 on 2021-05-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-07-03 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0021_merge_20200702_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='avatar',
        ),
    ]

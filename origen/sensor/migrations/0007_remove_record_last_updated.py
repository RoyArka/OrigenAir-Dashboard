# Generated by Django 3.0.6 on 2020-07-26 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0006_auto_20200726_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='last_updated',
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200618_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='person',
            name='position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.AddField(
            model_name='profile',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]

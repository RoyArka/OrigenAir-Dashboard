# Generated by Django 3.0.6 on 2020-07-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200714_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True, default='', max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='job_title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-07-03 18:45

from django.db import migrations, models
import organization.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0031_auto_20200703_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='org_avatar',
        ),
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, default='org/contemplating.png', null=True, upload_to=organization.models.org_directory_path),
        ),
    ]

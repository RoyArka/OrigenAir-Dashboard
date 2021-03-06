# Generated by Django 3.0.6 on 2020-07-29 20:19

from django.db import migrations, models
import organization.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0045_auto_20200728_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, default='org/default_org_logo.png', null=True, upload_to=organization.models.org_directory_path),
        ),
    ]

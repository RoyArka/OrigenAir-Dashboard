# Generated by Django 3.0.6 on 2020-07-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0015_auto_20200701_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0027_auto_20200703_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='org'),
        ),
    ]

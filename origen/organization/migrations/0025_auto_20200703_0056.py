# Generated by Django 3.0.7 on 2020-07-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0024_auto_20200702_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_avatar',
            field=models.ImageField(blank=True, default='media/placeholder.png', null=True, upload_to='org'),
        ),
    ]

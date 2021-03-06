# Generated by Django 3.0.6 on 2020-07-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20200701_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]

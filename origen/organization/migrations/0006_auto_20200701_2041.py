# Generated by Django 3.0.6 on 2020-07-02 03:41

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20200701_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='color',
            field=colorful.fields.RGBColorField(),
        ),
    ]

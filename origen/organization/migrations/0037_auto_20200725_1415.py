# Generated by Django 3.0.6 on 2020-07-25 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0036_auto_20200724_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_admin', to=settings.AUTH_USER_MODEL),
        ),
    ]

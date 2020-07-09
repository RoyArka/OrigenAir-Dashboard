# Generated by Django 3.0.6 on 2020-07-09 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0033_merge_20200703_1654'),
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='slug',
        ),
        migrations.AddField(
            model_name='sensor',
            name='threshold_max',
            field=models.CharField(default='100', max_length=100),
        ),
        migrations.AddField(
            model_name='sensor',
            name='threshold_min',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='values',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='organization.Organization'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('temperature', 'Temperature'), ('humidity', 'Humidity'), ('voc', 'Volatile Organic Compound'), ('co2', 'Carbon Dioxide')], default='None', max_length=100),
        ),
    ]

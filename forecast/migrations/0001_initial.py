# Generated by Django 5.1.1 on 2024-09-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservoir_name', models.CharField(max_length=255)),
                ('basin', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('full_reservoir_level', models.FloatField(blank=True, null=True)),
                ('live_capacity_frl', models.FloatField(blank=True, null=True)),
                ('storage', models.FloatField(blank=True, null=True)),
                ('level', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

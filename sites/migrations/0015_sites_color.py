# Generated by Django 5.1 on 2024-09-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0014_sites_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='color',
            field=models.CharField(blank=True, default='#007bff', max_length=7, null=True),
        ),
    ]
# Generated by Django 5.1 on 2024-08-30 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_image_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='plans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.plans'),
        ),
    ]

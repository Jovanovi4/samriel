# Generated by Django 5.1 on 2024-08-26 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_building_all_floor_remove_building_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.type'),
        ),
        migrations.AlterField(
            model_name='oldbuilding',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.type'),
        ),
    ]

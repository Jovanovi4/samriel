# Generated by Django 3.2.20 on 2024-08-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_building_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

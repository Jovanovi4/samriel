# Generated by Django 5.1 on 2024-09-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_image_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='total_area_from',
            field=models.FloatField(blank=True, null=True, verbose_name='Общая площадь от'),
        ),
        migrations.AlterField(
            model_name='plans',
            name='total_area_upto',
            field=models.FloatField(blank=True, null=True, verbose_name='Общая площадь до'),
        ),
    ]
# Generated by Django 5.1 on 2024-09-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_plans_total_area_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Отображать на сайте'),
        ),
    ]

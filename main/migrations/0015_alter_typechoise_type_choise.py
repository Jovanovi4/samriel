# Generated by Django 5.1 on 2024-08-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_building_down_description_alter_building_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typechoise',
            name='type_choise',
            field=models.CharField(choices=[('1', 'Комплексы (ЖК, Коттеджные поселки)'), ('2', 'Отдельные объекты (Вторичка, частные объявления)')], default='1', max_length=100, verbose_name='Тип недвижимости'),
        ),
    ]

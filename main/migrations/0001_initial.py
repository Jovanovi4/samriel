# Generated by Django 3.2.20 on 2024-08-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование объекта')),
                ('top_description', models.TextField(blank=True, null=True, verbose_name='Текст над названием')),
                ('down_description', models.TextField(blank=True, null=True, verbose_name='Текст под названием')),
                ('deadline', models.CharField(blank=True, max_length=255, null=True, verbose_name='Срок сдачи')),
                ('jarlyk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ярлык')),
                ('about_before_slide', models.TextField(blank=True, null=True, verbose_name='Описание до слайдера')),
                ('about_after_slide', models.TextField(blank=True, null=True, verbose_name='Описание после слайдера')),
                ('category', models.CharField(blank=True, choices=[('apartment', 'Квартира'), ('house', 'Дом'), ('dacha', 'Дача'), ('land', 'Земельный участок')], default='house', max_length=100, verbose_name='Категория недвижимости')),
            ],
        ),
    ]

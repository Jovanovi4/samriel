# Generated by Django 5.1 on 2024-08-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_image_alter_building_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='image_slider',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='building',
            name='image_slider',
            field=models.ImageField(blank=True, null=True, upload_to='slyder_images/', verbose_name='Фото слайдера'),
        ),
    ]
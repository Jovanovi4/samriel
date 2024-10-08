# Generated by Django 5.1 on 2024-09-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_alter_contact_instagram_link_alter_contact_vk_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='image',
            new_name='image_contacts',
        ),
        migrations.AlterField(
            model_name='contact',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на YouTube Канал'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vk_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на VK'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на Instagram'),
        ),
    ]

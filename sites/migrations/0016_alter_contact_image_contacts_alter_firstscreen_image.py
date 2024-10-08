# Generated by Django 5.1 on 2024-09-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0015_sites_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image_contacts',
            field=models.ImageField(blank=True, default='profile_images_contact/default_image_contacts.jpg', null=True, upload_to='profile_images_contact/'),
        ),
        migrations.AlterField(
            model_name='firstscreen',
            name='image',
            field=models.ImageField(blank=True, default='images/default_image.jpg', null=True, upload_to='images/'),
        ),
    ]

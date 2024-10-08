# Generated by Django 5.1 on 2024-09-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_plans_total_area_from_and_more'),
        ('sites', '0017_alter_contact_image_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='choise',
            name='selected_buildings',
            field=models.ManyToManyField(blank=True, related_name='choise_sites', to='main.building'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='image_contacts',
            field=models.ImageField(blank=True, default='profile_images_contact/free-icon-user-219983.png', null=True, upload_to='profile_images_contact/'),
        ),
    ]

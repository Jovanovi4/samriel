# Generated by Django 5.1 on 2024-09-03 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0008_alter_sites_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image_icons', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='image_contacts',
            field=models.ImageField(blank=True, default='profile_images_contact/default_image.jpg', null=True, upload_to='profile_images_contact/'),
        ),
        migrations.AddField(
            model_name='sites',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.logo'),
        ),
    ]

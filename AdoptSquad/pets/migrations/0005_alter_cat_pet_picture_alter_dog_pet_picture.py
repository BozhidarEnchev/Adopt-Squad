# Generated by Django 5.1.3 on 2024-11-28 14:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_cat_pet_picture_alter_dog_pet_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='pet_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pet_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]

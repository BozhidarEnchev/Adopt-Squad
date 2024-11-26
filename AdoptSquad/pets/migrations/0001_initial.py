# Generated by Django 5.1.3 on 2024-11-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('years', models.IntegerField(blank=True, null=True)),
                ('months', models.IntegerField(blank=True, null=True)),
                ('pet_picture', models.ImageField(upload_to='adopt-squad/pets/')),
                ('personality', models.CharField(choices=[('Playful', 'Playful'), ('Calm', 'Calm'), ('Unsocial', 'Unsocial'), ('Social', 'Social'), ('Energetic', 'Energetic')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('years', models.IntegerField(blank=True, null=True)),
                ('months', models.IntegerField(blank=True, null=True)),
                ('pet_picture', models.ImageField(upload_to='adopt-squad/pets/')),
                ('personality', models.CharField(choices=[('Playful', 'Playful'), ('Calm', 'Calm'), ('Unsocial', 'Unsocial'), ('Social', 'Social'), ('Energetic', 'Energetic')], max_length=50)),
                ('leash_trained', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
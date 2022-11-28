# Generated by Django 4.1.2 on 2022-11-27 23:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('video', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vaccination_observations', models.CharField(max_length=1000)),
                ('breed', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=10)),
            ],
        ),
    ]

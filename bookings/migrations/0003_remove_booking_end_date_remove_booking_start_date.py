# Generated by Django 4.1.2 on 2022-11-24 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_date',
        ),
    ]

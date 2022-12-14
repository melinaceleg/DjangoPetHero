# Generated by Django 4.1.2 on 2022-11-28 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_availability_booking'),
        ('bookings', '0004_alter_booking_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Availability',
        ),
        migrations.AddField(
            model_name='booking',
            name='availability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='users.availability'),
        ),
    ]

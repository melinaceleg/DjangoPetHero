# Generated by Django 4.1.2 on 2022-11-18 01:02

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Owner',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Keeper',
            fields=[
                ('owner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.owner')),
                ('pet_size', models.CharField(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], max_length=2)),
                ('keep_price', models.FloatField()),
            ],
            options={
                'verbose_name': 'Keeper',
            },
            bases=('users.owner',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('state', models.BooleanField(default=True)),
                ('keeper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.keeper')),
            ],
        ),
    ]

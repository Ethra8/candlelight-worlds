# Generated by Django 4.2 on 2024-06-09 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worlds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.CharField(choices=[('08:00', '08:00 - 12:00 AM'), ('12:00', '12:00 - 04:00 PM'), ('16:00', '04:00 - 08:00 PM'), ('20:00', '08:00 PM - 12:00 AM')], max_length=5)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worlds.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

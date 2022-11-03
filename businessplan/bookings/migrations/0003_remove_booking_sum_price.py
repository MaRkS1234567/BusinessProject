# Generated by Django 4.2.dev20220902080224 on 2022-10-07 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0002_booking_fullname_booking_pnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='sum',
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(verbose_name='Sum')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

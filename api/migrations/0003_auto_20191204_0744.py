# Generated by Django 2.2 on 2019-12-04 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191204_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='parking_spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='api.ParkingSpot'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-10 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_reservation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
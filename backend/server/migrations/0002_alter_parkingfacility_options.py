# Generated by Django 5.0.4 on 2024-04-05 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parkingfacility',
            options={'managed': False, 'ordering': ['FACILITY_NAME']},
        ),
    ]

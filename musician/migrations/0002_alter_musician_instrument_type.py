# Generated by Django 5.0.6 on 2024-06-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(choices=[('S', 'String'), ('W', 'Wind'), ('P', 'Percussion')], max_length=10),
        ),
    ]

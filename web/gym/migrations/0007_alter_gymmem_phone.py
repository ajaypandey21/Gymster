# Generated by Django 4.1.3 on 2023-01-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_trainer_gymmem_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmem',
            name='phone',
            field=models.CharField(default='91', max_length=30),
        ),
    ]
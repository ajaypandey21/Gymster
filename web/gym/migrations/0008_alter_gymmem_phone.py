# Generated by Django 4.1.3 on 2023-01-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_alter_gymmem_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmem',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
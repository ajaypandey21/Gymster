# Generated by Django 4.1.3 on 2023-01-11 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0018_gymmem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymmem',
            name='image',
        ),
    ]

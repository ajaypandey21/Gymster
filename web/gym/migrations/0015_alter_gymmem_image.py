# Generated by Django 4.1.3 on 2023-01-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0014_alter_gymmem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmem',
            name='image',
            field=models.ImageField(default='img.jpg', upload_to='myimage'),
        ),
    ]

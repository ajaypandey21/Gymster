# Generated by Django 4.1.3 on 2023-01-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_alter_gymmem_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymmem',
            name='image',
            field=models.ImageField(default='user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg', upload_to='myimage'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='t_id',
            field=models.IntegerField(),
        ),
    ]
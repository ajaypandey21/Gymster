# Generated by Django 4.1.3 on 2022-12-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [


    ]

    operations = [
        migrations.CreateModel(
            name='GymMem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]

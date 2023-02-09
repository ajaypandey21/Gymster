from django.db import models
from django.core import validators
from django import forms


# Create your models here.

class GymMem(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    program = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="myimage", null=True, blank=True)


class Admin(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Trainer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

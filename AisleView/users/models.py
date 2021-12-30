from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser (AbstractUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
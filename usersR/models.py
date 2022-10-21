from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    Nombre = models.CharField(max_length=15)

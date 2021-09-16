from django.db import models

from django.contrib.auth.models import AbstractUser, User
from django.forms import forms


class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

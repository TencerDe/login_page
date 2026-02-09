from django.db import models
from django.contrib.auth import login, logout
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    username = None #Removing username field for setting email as primary login method
    email = models.EmailField(unique=True, null=False, blank=False)
    iden = models.UUIDField(pk=True, default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False, help_text="Please verify yourself from your email before logging in")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

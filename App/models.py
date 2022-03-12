from django.db import models
from django.utils.translation import gettext_lazy
from django.utils import timezone
import os
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
import os


# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email"))
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(gettext_lazy("email address"), unique=True)
    name = models.CharField(max_length=200, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    secret = models.CharField(max_length=200, default="nothing")
    start_date = models.DateField(default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)+" "+str(self.email)


class Contact(models.Model):
    user = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name="usercontacts")
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "( "+self.name+" -> "+self.number+" ) created by "+self.user.name

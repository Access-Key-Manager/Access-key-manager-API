from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # todo: add other fields that are not on AbstractUser
    email = models.EmailField(_("Email Address"), blank=False, null=False, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # todo: add other fields that are not on AbstractUser
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email

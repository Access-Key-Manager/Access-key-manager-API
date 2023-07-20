from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from school.models import School

USER_MODEL = settings.AUTH_USER_MODEL


class User(AbstractUser):
    # todo: add other fields that are not on AbstractUser
    email = models.EmailField(_("Email Address"), blank=False, null=False, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email


class SchoolITPersonnel(models.Model):
    user = models.OneToOneField(
        USER_MODEL, on_delete=models.CASCADE, related_name="it_personnel"
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="it_personnel"
    )

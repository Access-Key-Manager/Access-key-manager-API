from django.db import models

# Create your models here.
from typing import Iterable, Optional
from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError


# to set date of procurement
import datetime

# to generate random tokens
import uuid
from school.models import School


# Create your models here.
class AccessKey(models.Model):
    class AccessKeyStatus(models.TextChoices):
        ACTIVATED = "ACTIVATED", "Activated"
        EXPIRED = "EXPIRED", "Expired"
        REVOKED = "REVOKED", "Revoked"
        NONE = "NONE", "None"

    status = models.CharField(
        choices=AccessKeyStatus.choices, default=AccessKeyStatus.NONE, max_length=10
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="access_keys"
    )
    procurement_date = models.DateField(
        blank=False, null=False, default=datetime.date.today
    )
    expiry_date = models.DateField(
        blank=False,
        null=False,
    )

    class PaymentStatus(models.TextChoices):
        MONTHLY = "MONTHLY", "Monthly"
        QUARTERLY = "QUARTERLY", "Quarterly"
        YEARLY = "YEARLY", "Yearly"

    key_duration = models.CharField(
        choices=PaymentStatus.choices, default=PaymentStatus.MONTHLY, max_length=10
    )
    token = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Token: {self.token}, Status: {self.status}"

    def save(self, *args, **kwargs) -> None:
        if (
            self.status == AccessKey.AccessKeyStatus.ACTIVATED
            and AccessKey.objects.filter(
                Q(school=self.school) & Q(status=AccessKey.AccessKeyStatus.ACTIVATED)
            ).count()
            >= 1
        ):
            raise ValidationError(
                "You can't have more than one activated Access Key. Please deactivate the existing one, or stop."
            )

        return super().save(*args, **kwargs)

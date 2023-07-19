from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class School(models.Model):
    class SchoolType(models.TextChoices):
        PUBLIC = "PUBLIC", "Public"
        PRIVATE = "PRIVATE", "Private"

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)

    school_type = models.CharField(
        choices=SchoolType.choices, default=SchoolType.PUBLIC, max_length=50
    )
    num_of_users = models.IntegerField(
        default=1, validators=[MaxValueValidator(1), MinValueValidator(1)]
    )

    def __str__(self) -> str:
        return self.name

    @property
    def all_access_keys(self):
        return self.access_keys.all()

from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Hotels(models.Model):

    ville = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    
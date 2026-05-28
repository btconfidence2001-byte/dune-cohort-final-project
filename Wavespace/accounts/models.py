from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        BUYER = 'BUYER', 'Buyer'
        SELLER = 'SELLER', 'Seller'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.BUYER,
    )

    @property
    def is_buyer(self):
        if self.is_staff or self.is_superuser:
            return False
        return self.role == self.Role.BUYER

    @property
    def is_seller(self):
        if self.is_staff or self.is_superuser:
            return False
        return self.role == self.Role.SELLER

    def save(self, *args, **kwargs):
        if self.role:
            self.role = self.role.upper()
        super().save(*args, **kwargs)

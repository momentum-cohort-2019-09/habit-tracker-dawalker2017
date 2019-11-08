from django.db import models
from django.contrib.auth.models import AbstractUser

#===========================================| User class |=========================================#
class User(AbstractUser):
    pass

#===========================================| Habit class |=========================================#
class Habit(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="habits",
        )

    subject = models.CharField(
        max_length=25,
        verbose_name="Subject:",
        blank=False,
        null=True,
        help_text="Max Characters: 25"
        )

    description = models.CharField(
        max_length=255,
        verbose_name="Description:",
        blank=False,
        null=True,
        help_text="Max Characters: 255",
        )

    created_at = models.DateTimeField(
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        auto_now=True,
        )

    is_active = models.BooleanField(
        default=True,
        )

    def __str__(self):
        return self.subject
    def __str__(self):
        return self.description
    def __str__(self):
        return self.created_at
    def __str__(self):
        return self.updated_at
    def __str__(self):
        return self.is_active
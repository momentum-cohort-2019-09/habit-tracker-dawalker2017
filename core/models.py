from django.db import models
from django.contrib.auth.models import AbstractUser

#===========================================| User class |=========================================#
class User(AbstractUser):
    pass

#===========================================| Log class |=========================================#
class Log(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="logs",
        )

    subject = models.CharField(
        max_length=50,
        verbose_name="Subject:",
        blank=False,
        null=True,
        help_text="Max Characters: 50"
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
    
    Habits_completed = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return self.subject
    def number_of_habits(self):
        return self.habits.count()

#===========================================| Habit class |=========================================#
class Habit(models.Model):
    log = models.ForeignKey(
        to=Log,
        on_delete=models.CASCADE,
        related_name="habits"
        )

    title = models.CharField(
        max_length=255,
        verbose_name="Title:",
        blank=False,
        null=True,
        help_text="Max Characters: 255"
        )

    description = models.TextField(
        max_length=255,
        verbose_name="Description:",
        blank=True,
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
        return self.title
    def __str__(self):
        return self.description
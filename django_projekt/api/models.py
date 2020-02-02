from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    """Model definition for Profile ."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    class Meta:
        """Meta definition for Profile ."""

        verbose_name = 'Profil '
        verbose_name_plural = 'Profile '

    def __str__(self):
        """Unicode representation of Profile ."""
        return f'{self.user.username} Profile'

    

    # TODO: Define custom methods here


from django.db import models
from django.contrib.auth.models import AbstractUser
from SmartPot import settings

class AppUser(AbstractUser):
    moisture_preference = models.SmallIntegerField(default=0)

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='history', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    moisture = models.DecimalField(default=None, null=True, decimal_places=2, max_digits=6)
    temperature = models.IntegerField(default=None, null=True)
    # humidity = models.DecimalField(default=None, null=True, decimal_places=2, max_digits=6)
    light = models.IntegerField(default=None, null=True)

from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import DecimalField
from django.utils import timezone
import datetime
# Create your models here.

# Create your models here.
class Prospect(models.Model):
    name = models.CharField(max_length=255, null=True, default = "")
    city = models.CharField(max_length=255, null=True)
    schoolOfOrigin = models.CharField(max_length=255, null=True)
    graduateArea = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = JSONField()
    socialMedia = JSONField()
    townShip = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "prospect"

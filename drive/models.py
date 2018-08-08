from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import DecimalField
from django.utils import timezone
import datetime
# Create your models here.
class Drive(models.Model):
    name = models.CharField(max_length = 255, null=True)
    originalName = models.CharField(max_length = 255, null=True)
    size = models.CharField(max_length = 255, null=True)
    url = models.ImageField(blank=False, null=False)
    fileType = models.CharField(max_length=255, null=True)
    tags = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "drive"

#
class userDrive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    remove = models.BooleanField(default = False)

    class Meta:
        db_table = "userDrive"
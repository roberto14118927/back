from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import DecimalField
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
import datetime
# fs = FileSystemStorage(location='media/')
# Created your models here.
class Institution(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    controlNumber = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=355, null=True)
    zipCode = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    businessName = models.CharField(max_length=255, null=True)
    rfc = models.CharField(max_length=255, null=True)
    businessAddress = models.CharField(max_length=255, null=True)
    businessInitDate = models.DateTimeField(blank=True, null=True, default=None) # models.DateTimeField(default=datetime.date.today)
    parentId = models.IntegerField(null=True, default=0)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "institution"


class catEducationType(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution,  on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catEducationType"

class catEducationLevel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    catEducationType = models.ForeignKey(catEducationType,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=355, null=True)
    phone = JSONField(null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catEducationLevel"

class catEducationArea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    catEducationLevel = models.ForeignKey(catEducationLevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    abbreviation = models.CharField(max_length=155, null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catEducationArea"

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    catEducationLevel = models.ForeignKey(catEducationLevel, default=None, on_delete=models.CASCADE)
    #catEducationAreaId = models.ForeignKey(catEducationArea, default=None, on_delete=models.CASCADE)
    #catEducationArealId = models.IntegerField(null=True, default=0)
    educationLogo = models.ImageField(upload_to='media/', null=True, blank=True)
    name = models.CharField(max_length=150, null=True)
    shortName = models.CharField(max_length=255, null=True)
    acronym = models.CharField(max_length=15, null=True)
    durationMonths = models.IntegerField(null=True, default=0)
    # studycode = models.CharField(max_length=255, null=True)
    # studycodeauthdate = models.DateTimeField(blank=True, null=True, default=None)
    created = models.DateTimeField(default = timezone.now)
    delete = models.BooleanField(default = False)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "education"

class catSchoolCycle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    isCurrent = models.BooleanField(default = False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catSchoolCycle"

class catSchoolPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    acronym = models.CharField(max_length=15, null=True)
    monthNumber = models.IntegerField(null=True)
    initMonth = models.DateField(blank=True, null=True, default=None)
    endMonth = models.DateField(blank=True, null=True, default=None)
    isCurrent = models.BooleanField(default = False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catSchoolPeriod"


class catEducationSystem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    daysNumber = models.IntegerField(null=True)
    days = JSONField(null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catEducationSystem"

class educationHasSystem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    catEducationSystem = models.ForeignKey(catEducationSystem, on_delete=models.CASCADE)
    studyCode = models.CharField(max_length=255, null=True)
    studyCodeAuthDate = models.DateField(blank=True, null=True, default=None)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __unicode__(self):
        return u"%s" % self.educationHasSystem
    
    class Meta:
        db_table = "educationHasSystem"
    
    

class catSchoolShift(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    initTime = models.DateField(blank=True, null=True, default=None)
    endTime = models.DateField(blank=True, null=True, default=None)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catSchoolShift"

class educationStudyPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    initDate = models.DateField(blank=True, null=True, default=None)
    isActive = models.BooleanField(default = False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "educationStudyPlan"

class educationConfigPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    educationSystem = models.ForeignKey(catEducationSystem, on_delete=models.CASCADE)
    catSchoolShift = models.ForeignKey(catSchoolShift, on_delete=models.CASCADE)
    catSchoolCycle = models.ForeignKey(catSchoolCycle, on_delete=models.CASCADE)
    catSchoolPeriod = models.ForeignKey(catSchoolPeriod, on_delete=models.CASCADE)
    educationPlan = models.ForeignKey(educationStudyPlan, on_delete=models.CASCADE)
    generation = models.BigIntegerField(null=True)
    period = models.BigIntegerField(null=True)
    isCurrent = models.BooleanField(default = False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return str(self.generation)

    class Meta:
        db_table = "educationCurrentPeriod"

class catDocumentRequired(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "catDocumentRequired"

class educationHasDocumentRequired(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    catDocumentRequired = models.ForeignKey(catDocumentRequired,on_delete=models.CASCADE)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.educationHasDocumentRequiredId

    class Meta:
        db_table = "educationHasDocumentRequired"

class catCountry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    countryName = models.CharField(max_length=255, null=True)
    countryCode = models.CharField(max_length=15, null=True)
    comment = models.TextField(null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.countryName

    class Meta:
        db_table = "catCountry"

class catState(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    catCountry = models.ForeignKey(catCountry, on_delete=models.CASCADE)
    stateName = models.CharField(max_length=255, null=True)
    stateCode = models.CharField(max_length=15, null=True)
    comment = models.TextField(null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.stateName

    class Meta:
        db_table = "catState"


class catCity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    catState = models.ForeignKey(catState, on_delete=models.CASCADE)
    cityName = models.CharField(max_length=255, null=True)
    cityCode = models.CharField(max_length=15, null=True)
    comment = models.TextField(null=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.cityName

    class Meta:
        db_table = "catCity"

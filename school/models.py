from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from globalsettings.models import Education, educationStudyPlan, catSchoolPeriod, educationConfigPeriod

# Create your models here.
class catSchoolGrade(models.Model):
    gradeNumber = models.IntegerField(null=True, default=0)
    name = models.CharField(max_length=255, null=True)
    shortName = models.CharField(max_length=15, null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.IntegerField(null=True, blank=True)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "catSchoolGrade"

class catSchoolWeekDay(models.Model):
    name = models.CharField(max_length=255, null=True)
    shortName = models.CharField(max_length=15, null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.IntegerField(null=True, blank=True)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "catSchoolWeekDay"


class catSchoolOfOriginLevel(models.Model):
    levelName = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.IntegerField(null=True, blank=True)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.levelName

    class Meta:
        db_table = "catSchoolOriginLevel"

class schoolOfOrigin(models.Model):
    schoolName = models.CharField(max_length=255, null=True)
    catSchoolOriginLevel = models.ForeignKey(catSchoolOfOriginLevel, on_delete=models.DO_NOTHING)
    schoolCityId = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    postalCode = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    webSite = models.CharField(max_length=255, null=True)
    lat = models.CharField(max_length=20, null=True)
    lon = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(default = timezone.now)
    user = models.IntegerField(null=True, blank=True)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.schoolName

    class Meta:
        db_table = "schoolOfOrigin"

#another model
class schoolMateria(models.Model):
    name = models.CharField(max_length = 255, null = True)
    credit = models.FloatField(null = True)
    minHoursAWeek = models.IntegerField(null=True, default = 0)
    useLaboratory = models.BooleanField(default = False)
    laboratoryHours = models.IntegerField(null=True, default = 0)
    onlyTheory = models.BooleanField(default = False)
    percentTheory = models.FloatField(null = True, default = 0)
    percentPractice = models.FloatField(null = True, default = 0)
    order = models.IntegerField(null = True, default = 0)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.IntegerField(null=True, default = 0)
    remove = models.BooleanField(default = False)
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING)
    educationStudyPlan = models.ForeignKey(educationStudyPlan, on_delete=models.DO_NOTHING)
    catSchoolGrade = models.ForeignKey(catSchoolGrade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "schoolMateria"

#student parent
class studentParent(models.Model):
    name = models.CharField(max_length = 255, null = True)
    lastName = models.CharField(max_length = 255, null = True)
    phone = JSONField(null = True)
    address = models.TextField(null = True, blank = True)
    email = models.EmailField(null = True, blank=True)
    typeParent = models.CharField(max_length = 50, null=True)
    isTutor = models.BooleanField(default=False)
    maxStudyGrade = models.CharField(max_length = 255, null=True)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length = 255, null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.IntegerField(null = True, default = 0)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "studentParent"

#another model
class schoolGroup(models.Model):
    educactionPeriod = models.ForeignKey(educationConfigPeriod, on_delete=models.DO_NOTHING)
    catSchoolGrade = models.ForeignKey(catSchoolGrade, on_delete = models.DO_NOTHING)
    acronym = models.CharField(max_length = 15, null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    user = models.IntegerField(null=True, default = 0)
    remove = models.BooleanField(default = False)

    def __str__(self):
        return self.acronym

    class Meta:
        db_table = "schoolGroup"

#another model
class schoolGroupMateriaStudent(models.Model):
    schoolGroup = models.ForeignKey(schoolGroup, on_delete = models.CASCADE)
    schoolMateria = models.ForeignKey(schoolMateria, on_delete = models.CASCADE)
    isPartial = models.BooleanField(default = False)
    scoreNumber = models.IntegerField(null = True, default = 0)
    theoryScore = models.FloatField(null = True)
    practiceScore = models.FloatField(null = True)
    finalScore = models.FloatField(null = True)
    user = models.IntegerField(null = True, default = 0)
    remove = models.BooleanField(default = False)

    class Meta:
        db_table = "schoolGroupMateriaStudent"

#another model
class schoolTeacherDisponibility(models.Model):
    schoolPeriod = models.ForeignKey(catSchoolPeriod, on_delete = models.CASCADE)
    user = models.IntegerField(null = True, default = 0)
    schedule = JSONField(null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    remove = models.BooleanField(default = False)

    class Meta:
        db_table = "schoolTeacherDisponibility"
#another model
class schoolTeacherHasMateria(models.Model):
    schoolMateria = models.ForeignKey(schoolMateria, on_delete = models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.IntegerField(null=True, default = 0)
    remove = models.BooleanField(default = False)

    class Meta:
        db_table = "schoolTeacherHasMateria"
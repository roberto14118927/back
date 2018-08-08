# -----------------LIBRERIAS----------------------
from rest_framework import routers, serializers, viewsets

# -----------------MODELOS----------------------
from globalsettings.models import Institution
from globalsettings.models import catEducationType
from globalsettings.models import catEducationLevel
from globalsettings.models import catEducationArea
from globalsettings.models import Education
from globalsettings.models import catSchoolCycle
from globalsettings.models import catSchoolPeriod
from globalsettings.models import catEducationSystem
from globalsettings.models import educationHasSystem
from globalsettings.models import catSchoolShift


class InstitutionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'user', 'name', 'controlNumber', 'address', 'zipCode', 'city', 'state', 'logo', 
                'businessName', 'rfc', 'businessAddress', 'businessInitDate', 'parentId', 'delete')
# -------------------------------------------------------------------------------------------
class EducationTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = catEducationType
        fields = ('id', 'user', 'institution', 'name', 'delete')
# -------------------------------------------------------------------------------------------
class catEducationLevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = catEducationLevel
        fields = ('id', 'user', 'catEducationType', 'name', 'address', 'phone', 'delete')
# -------------------------------------------------------------------------------------------
class catEducationAreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = catEducationArea
        fields = ('id', 'user', 'catEducationLevel', 'name', 'abbreviation', 'delete')
# -------------------------------------------------------------------------------------------
class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'user', 'catEducationLevel', 'educationLogo', 'name', 'shortName', 'acronym', 'durationMonths', 'delete')
# -------------------------------------------------------------------------------------------
class CatSchoolCycleSerializers(serializers.ModelSerializer):
    class Meta:
        model = catSchoolCycle
        fields = ('id', 'user', 'name', 'isCurrent', 'delete')
# -------------------------------------------------------------------------------------------
class CatSchoolPeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = catSchoolPeriod
        fields = ('id', 'user', 'name', 'acronym', 'monthNumber', 'initMonth', 'endMonth', 'isCurrent', 'delete')
# -------------------------------------------------------------------------------------------
class catEducationSystemSerializers(serializers.ModelSerializer):
    class Meta:
        model = catEducationSystem
        fields = ('id', 'user', 'name', 'daysNumber', 'days', 'delete')

class catEducationSystemSerializers(serializers.ModelSerializer):
    class Meta:
        model = catEducationSystem
        fields = ('id', 'user', 'education', 'catEducationSystem', 'studyCode', 'studyCodeAuthDate', 'delete')

class catSchoolShiftSerializers(serializers.ModelSerializer):
    class Meta:
        model = catSchoolShift
        fields = ('id', 'user', 'initTime', 'endTime', 'delete')
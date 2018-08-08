from rest_framework import serializers
from school.models import catSchoolGrade, catSchoolWeekDay, catSchoolOfOriginLevel, schoolOfOrigin, schoolMateria, schoolGroup, schoolGroupMateriaStudent, schoolTeacherDisponibility, studentParent

class JSONSerializerField(serializers.Field):
    """ Serializer para JSONField -- requiere hacer el campo escribible """
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value

class schoolGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = catSchoolGrade
        fields = ('name', 'shortName', 'id', 'gradeNumber', 'edited')

class schoolWeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = catSchoolWeekDay
        fields = ('name', 'shortName', 'id', 'edited')

class schoolOfOriginLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = catSchoolOfOriginLevel
        fields = ('id', 'levelName', 'edited')

class schoolOfOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolOfOrigin
        fields = ('id', 'schoolName', 'address', 'postalCode', 'phone', 'email', 'webSite', 'lat', 'lon', 'edited')

class schoolMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolMateria
        fields = ('id', 'name', 'credit', 'minHoursAWeek', 'useLaboratory', 'laboratoryHours', 'onlyTheory', 'percentTheory', 'percentPractice', 'order', 'education', 'educationStudyPlan', 'catSchoolGrade', 'edited')

class schoolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolGroup
        fields = ('educactionPeriod', 'catSchoolGrade', 'acronym', 'edited', 'user', 'remove')

#
class schoolGroupMateriaStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolGroupMateriaStudent
        fields = ('schoolGroup','schoolMateria','isPartial','scoreNumber', 'theoryScore', 'practiceScore', 'finalScore', 'user', 'remove')

class schoolTeacherDisponibilitySerializer(serializers.ModelSerializer):
    schedule = JSONSerializerField()
    class Meta:
        model = schoolTeacherDisponibility
        fields = ('schoolPeriod', 'user', 'schedule', 'created', 'edited', 'remove')

class studentParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentParent
        fields = ('id', 'name', 'lastName', 'phone', 'address', 'email', 'typeParent', 'isTutor', 'maxStudyGrade', 'age', 'occupation', 'created', 'edited', 'user', 'remove')
from rest_framework import serializers
from leads.models import Prospect

class JSONSerializerField(serializers.Field):
    """ Serializer para JSONField -- requiere hacer el campo escribible """
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value

class contactSerializer(serializers.ModelSerializer):
    phone = JSONSerializerField()
    class Meta:
        model = Prospect
        fields = ('id','name', 'city', 'schoolOfOrigin', 'graduateArea', 'email', 'phone', 'townShip', 'socialMedia')
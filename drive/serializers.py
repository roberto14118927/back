from rest_framework import serializers
from drive.models import Drive, userDrive

class driveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = ('name', 'originalName', 'size', 'url', 'fileType', 'tags', 'created', 'edited', 'user', 'id', 'remove')

class userDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDrive
        fields = ('user', 'drive', 'id')

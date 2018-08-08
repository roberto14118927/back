from django.shortcuts import render
from django.http import HttpResponse, Http404
#add frameworks imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from drive.serializers import driveSerializer, userDriveSerializer
from drive.models import Drive, userDrive
# Create your views here.
class driveList(APIView):
    """
    LIST ALL DRIVE OR CREATE  A NEW DRIVE
    """
    def get(self, request, format = None):
        queryset = Drive.objects.filter(remove=False)
        if queryset:
            serializer = driveSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            content = {'204':'No hay contentido'}
            return Response(content, status = status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = driveSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        drive = self.get_object(id)
        drive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class driveDetail(APIView):
    """
    RETRIEVE, UPDATE, DELETE A DRIVE INSTANCE
    """
    def get_object(self, id):
        try:
            return Drive.objects.get(id=id)
        except Drive.DoesNotExist:
            return 404


    def get(self, request, id, format=None):
        drive = self.get_object(id)
        serializer = driveSerializer(drive)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        if request.method == 'PUT':
            drive = self.get_object(id)
            serializer = driveSerializer(drive, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        if request.method == 'DELETE':
            stdrive = self.get_object(id)
            if stdrive == 404:
                content = {'404': 'No se encontró el Id asociado'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                stdrive.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

class userDriveList(APIView):
    """
    LIST ALL USER DRIVE OR CREATE  A NEW DRIVE
    """
    def get(self, request, format=None):
        queryset = userDrive.objects.filter(remove=False)
        if queryset:
            serializer = userDriveSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            content = {'204':'No hay contentido'}
            return Response(content, status = status.HTTP_204_NO_CONTENT)
    
    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = userDriveSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        userdrive = self.get_object(id)
        userdrive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class detail user drive
class userDriveDetail(APIView):
    """
    RETRIEVE, UPDATE, DELETE A USER DRIVE INSTANCE
    """
    def get_object(self, id):
        try:
            return userDrive.objects.get(id=id)
        except expression as identifier:
            return 404

    def get(self, request, id, format=None):
        userDrive = self.get_object(id)
        serializer = userDriveSerializer(userDrive)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        if request.method == 'PUT':
            driveUser = self.get_object(id)
            serializer = userDriveSerializer(driveUser, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        if request.method == 'DELETE':
            userDrive = self.get_object(id)
            if userDrive == 404:
                content = {'404': 'No se encontró el Id asociado'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                userDrive.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
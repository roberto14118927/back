# -----------------LIBRERIAS----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

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

# -----------------SERIALIZERS----------------------
from globalsettings.serializers import InstitutionSerializers
from globalsettings.serializers import EducationTypeSerializers
from globalsettings.serializers import catEducationLevelSerializers
from globalsettings.serializers import catEducationAreaSerializers
from globalsettings.serializers import EducationSerializers
from globalsettings.serializers import CatSchoolCycleSerializers
from globalsettings.serializers import CatSchoolPeriodSerializers
from globalsettings.serializers import catEducationSystemSerializers
import json

class InstitutionList(APIView):
    def get(self, request, format=None):
        queryset = Institution.objects.filter(delete = False)
        serializer = InstitutionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstitutionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class InstitutionDetail(APIView):
    def get_object(self, pk):
        try:
            return Institution.objects.get(pk=pk)
        except Institution.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = InstitutionSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = InstitutionSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class EducationTypeList(APIView):
    def get(self, request, format=None):
        queryset = catEducationType.objects.filter(delete = False)
        serializer = EducationTypeSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EducationTypeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class EducationTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return catEducationType.objects.get(pk=pk)
        except catEducationType.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = EducationTypeSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = EducationTypeSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class CatEducationLevelList(APIView):
    def get(self, request, format=None):
        queryset = catEducationLevel.objects.filter(delete = False)
        serializer = catEducationLevelSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = catEducationLevelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class CatEducationLevelDetail(APIView):
    def get_object(self, pk):
        try:
            return catEducationLevel.objects.get(pk=pk)
        except catEducationLevel.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = catEducationLevelSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = catEducationLevelSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class CatEducationAreaList(APIView):
    def get(self, request, format=None):
        queryset = catEducationArea.objects.filter(delete = False)
        serializer = catEducationAreaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = catEducationAreaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class CatEducationAreaDetail(APIView):
    def get_object(self, pk):
        try:
            return catEducationArea.objects.get(pk=pk)
        except catEducationArea.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = catEducationAreaSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = catEducationAreaSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class EducationList(APIView):
    def get(self, request, format=None):
        queryset = Education.objects.filter(delete = False)
        serializer = EducationSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EducationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class EducationDetail(APIView):
    def get_object(self, pk):
        try:
            return Education.objects.get(pk=pk)
        except Education.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = EducationSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = EducationSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class CatSchoolCycleList(APIView):
    def get(self, request, format=None):
        queryset = catSchoolCycle.objects.filter(delete = False)
        serializer = CatSchoolCycleSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CatSchoolCycleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class CatSchoolCycleDetail(APIView):
    def get_object(self, pk):
        try:
            return catSchoolCycle.objects.get(pk=pk)
        except catSchoolCycle.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = CatSchoolCycleSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = CatSchoolCycleSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class CatSchoolPeriodList(APIView):
    def get(self, request, format=None):
        queryset = catSchoolPeriod.objects.filter(delete = False)
        serializer = CatSchoolPeriodSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CatSchoolPeriodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class CatSchoolPeriodDetail(APIView):
    def get_object(self, pk):
        try:
            return catSchoolPeriod.objects.get(pk=pk)
        except catSchoolPeriod.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = CatSchoolPeriodSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = CatSchoolPeriodSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------
class CatEducationSystemList(APIView):
    def get(self, request, format=None):
        queryset = catEducationSystem.objects.filter(delete = False)
        serializer = catEducationSystemSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = catEducationSystemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class CatEducationSystemDetail(APIView):
    def get_object(self, pk):
        try:
            return catEducationSystem.objects.get(pk=pk)
        except catEducationSystem.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = catEducationSystemSerializers(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = catEducationSystemSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson("Error", "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------







def repuestaJson(success, datas, message):
    respuesta = '{'
    respuesta += '"status"'
    respuesta += ":"
    respuesta += '"'+str(success)+'"'
    respuesta += ","

    respuesta += '"data"'
    respuesta += ":"
    respuesta += '"'+str(datas)+'"'
    respuesta += ","

    respuesta += '"message"'
    respuesta += ":"
    respuesta += '"'+str(message)+'"'

    respuesta += '}'
    respuesta = json.loads(respuesta)

    return(respuesta)




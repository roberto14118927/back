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
from school.models import catSchoolGrade, catSchoolWeekDay, catSchoolOfOriginLevel, schoolOfOrigin, schoolMateria, schoolGroup, schoolGroupMateriaStudent, schoolTeacherDisponibility, studentParent
from school.serializer import schoolGradeSerializer, schoolWeekDaySerializer, schoolOfOriginLevelSerializer, schoolOfOriginSerializer, schoolMateriaSerializer, schoolGroupSerializer, schoolGroupMateriaStudentSerializer, schoolTeacherDisponibilitySerializer, studentParentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@permission_classes((IsAuthenticated, ))
class schoolGradeList(generics.ListCreateAPIView):
    queryset = catSchoolGrade.objects.filter(remove=False)
    serializer_class = schoolGradeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolGradeSerializer(queryset, many=True)
        return Response(serializer.data)

@permission_classes((IsAuthenticated, ))
class schoolGradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = catSchoolGrade.objects.all()
    lookup_field = 'id'
    serializer_class = schoolGradeSerializer

class schoolWeekDayList(generics.ListCreateAPIView):
    queryset = catSchoolWeekDay.objects.filter(remove=False)
    serializer_class = schoolWeekDaySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolWeekDaySerializer(queryset, many=True)
        return Response(serializer.data)

class schoolWeekDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = catSchoolWeekDay.objects.all()
    lookup_field = 'id'
    serializer_class = schoolWeekDaySerializer
#
class schoolOriginLevelList(generics.ListCreateAPIView):
    queryset = catSchoolOfOriginLevel.objects.filter(remove=False)
    serializer_class = schoolOfOriginLevelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolOfOriginLevelSerializer(queryset, many=True)
        return Response(serializer.data)
#
class schoolOriginLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = catSchoolOfOriginLevel.objects.all()
    lookup_field = 'id'
    serializer_class = schoolOfOriginLevelSerializer

#
class schoolOfOriginList(generics.ListCreateAPIView):
    queryset = schoolOfOrigin.objects.filter(remove=False)
    serializer_class = schoolOfOriginSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolOfOriginSerializer(queryset, many=True)
        return Response(serializer.data)

class schoolOfOriginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = schoolOfOrigin.objects.all()
    lookup_field = 'id'
    serializer_class = schoolOfOriginSerializer

#add new classes
class schoolMateriaList(generics.ListCreateAPIView):
    queryset = schoolMateria.objects.filter(remove=False)
    serializer_class = schoolMateriaSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolMateriaSerializer(queryset, many=True)
        return Response(serializer.data)

class schoolMateriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = schoolMateria.objects.all()
    lookup_field = 'id'
    serializer_class = schoolMateriaSerializer

#new classes
class schoolGroupList(generics.ListCreateAPIView):
    queryset = schoolGroup.objects.filter(remove=False)
    serializer_class = schoolGroupSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolGroupSerializer(queryset, many=True)
        return Response(serializer.data)

class schoolGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = schoolGroup.objects.all()
    lookup_field = 'id'
    serializer_class = schoolGroupSerializer

class schoolGroupMateriaStudentList(generics.ListCreateAPIView):
    queryset = schoolGroupMateriaStudent.objects.filter(remove = True)
    serializer_class = schoolGroupMateriaStudentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolGroupMateriaStudentSerializer(queryset, many=True)
        return Response(serializer.data)

class schoolGroupMateriaStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = schoolGroupMateriaStudent.objects.all()
    lookup_field = 'id'
    serializer_class = schoolGroupMateriaStudentSerializer


class schoolTeacherDisponibilityList(generics.ListCreateAPIView):
    queryset = schoolTeacherDisponibility.objects.filter(remove = True)
    serializer_class = schoolTeacherDisponibilitySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = schoolTeacherDisponibilitySerializer(queryset, many=True)
        return Response(serializer.data)

class schoolTeacherDisponibilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = schoolTeacherDisponibility.objects.all()
    lookup_field = 'id'
    serializer_class = schoolTeacherDisponibility
    
class studentParentList(APIView):
    """
      List all student Parents or create a new Parent
    """
    def get(self, request, format=None):
        queryset = studentParent.objects.filter(remove=False)
        if queryset:
            serializer = studentParentSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            content = {'please move along': 'No hay registros'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = studentParentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        studentparent = self.get_object(pk)
        studentParent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class studentParentDetail(APIView):
    """
     retrieve, update or delete a studentParent instance
    """
    def get_object(self, id):
        try:
            return studentParent.objects.get(id=id)
        except studentParent.DoesNotExist:
            return 404
        
    def get(self, request, id, format=None):
        studentparent = self.get_object(id)
        serializer = studentParentSerializer(studentparent)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        if request.method == 'PUT':
            studentparents = self.get_object(id)
            serializer = studentParentSerializer(studentparents, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        if request.method == 'DELETE':
            stdparent = self.get_object(id)
            if stdparent == 404:
                content = {'404': 'No se encontró el Id asociado'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                stdparent.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
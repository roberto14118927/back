from django.shortcuts import render
from django.http import HttpResponse
#add frameworks imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from leads.models import Prospect
from leads.serializer import contactSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
def prospect_list(request):

    if request.method == 'GET':
        prospects = Prospect.objects.all()
        serializer = contactSerializer(prospects, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = contactSerializer(data = data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def prospect_detail(request, pk):
    """
    recuperar, actualizar o borrar un prospecto
    """
    try:
        prospect = Prospect.objects.get(id = pk)
    except Prospect.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = contactSerializer(prospect)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = contactSerializer(prospect, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prospect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


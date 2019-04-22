from django.shortcuts import render
from .models import employee
from .serializer import REST_DATA
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hi Pradip, Welcome to Rest API.</h1>')

@api_view(['GET','POST'])
def GETPOST(request):

    if request.method == 'GET':

        data = employee.objects.all()
        serializer = REST_DATA(data, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = REST_DATA(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def GETPUTDELETE(request,emp_id):

    try:

        data1 = employee.objects.get(pk=emp_id)

    except :
        return HttpResponse("<h3>Employee Id not found:<h3>")

    if request.method == 'GET':
        serializer = REST_DATA(data1)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = REST_DATA(data1, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        data1.delete()

        return Response(status=status.HTTP_200_OK)




from functools import partial
from django.shortcuts import render
import requests
from requests import status_codes
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET','post','put','patch','delete'])
def student_api(request,pk=None):
    if request.method=='GET':
        stu_id = pk
        if stu_id is not None:
            stu=Student.objects.get(id=stu_id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg={'Succussful':'Your data has been secussfully updated'}
            return Response(msg ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        stu_id=pk
        stu_instance=Student.objects.get(id=stu_id)
        serializer=StudentSerializer(stu_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success':'Data updated Partically'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PATCH':
        stu_id=pk
        stu_instance=Student.objects.get(id=stu_id)
        serializer=StudentSerializer(stu_instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success':'Data updated Partically'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='DELETE':
        stu_id=pk
        stu_obj=Student.objects.get(id=stu_id)
        stu_obj.delete()
        return Response({'Delete':'Data has been deleted'},status=status.HTTP_201_CREATED)
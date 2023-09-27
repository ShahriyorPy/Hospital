from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.


class XonalarAPIView(APIView):
    def get(self, request):
        xonalar = Xona.objects.all()
        serializer = XonaSerializer(xonalar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = XonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class XonaAPIView(APIView):
    def get(self, request, pk):
        xona = Xona.objects.get(id=pk)
        serializer = XonaSerializer(xona)
        return Response(serializer.data)

    def delete(self, instance, pk):
        xona = XonaSerializer.objects.filter(id=pk).delete()
        data = {
            "success": True,
            "xabar": "Xona o'chirildi!"
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        xona = Xona.objects.get(id=pk)
        serializer = XonaSerializer(xona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
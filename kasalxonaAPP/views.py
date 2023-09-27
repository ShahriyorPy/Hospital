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
        qarovchisi = request.query_params.get("qarovchi")
        if qarovchisi:
            xonalar = Xona.objects.filter(bosh_joy_soni__gt=1)
        else:
            xonalar = Xona.objects.filter(bosh_joy_soni__gt=0)
        serializer = XonaSerializer(xonalar,many=True)
        return Response(serializer.data)


class XonaAPIView(APIView):
    def get(self, request, pk):
        xona = Xona.objects.get(id=pk)
        serializer = XonaSerializer(xona)
        return Response(serializer.data)

    def put(self, request, pk):
        xona = Xona.objects.get(id=pk)
        serializer = XonaSerializer(xona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
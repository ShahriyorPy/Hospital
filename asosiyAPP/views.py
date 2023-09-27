from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.


class BemorlarAPIView(APIView):
    def get(self, request):
        bemorlar = Bemor.objects.all()
        qidiruv = request.query_params.get("qidiruv")  # /?qidiruv
        joylashish = request.query_params.get("joylashgan")  # /?joylashgan
        qarzdor = request.query_params.get("qarzdor")  # /?qarzdor
        if qidiruv:
            bemorlar = Bemor.objects.filter(ism__contains=qidiruv
            )| Bemor.objects.filter(tel__contains=qidiruv
            )| Bemor.objects.filter(manzil__contains=qidiruv
            )| Bemor.objects.filter(sana__contains=qidiruv)
        if joylashish:
            if joylashish == 'true':
                bemorlar = bemorlar.filter(joylashgan=True)
            else:
                bemorlar = bemorlar.filter(joylashgan=False)
        if qarzdor:
            if qarzdor == "true":
                tolovlar = Tolov.objects.filter(tolandi=False).values("bemor").distinct()
            else:
                tolovlar = Tolov.objects.filter(tolandi=True).values("bemor").distinct()
            bemorlar = bemorlar.filter(id__in=tolovlar)
        serializer = BemorSerializer(bemorlar, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = BemorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class BemorAPIView(APIView):
    def get(self, request, pk):
        bemor = Bemor.objects.get(id=pk)
        serializer = BemorSerializer(bemor)
        return Response(serializer.data)

    def delete(self, instance, pk):
        bemor = Bemor.objects.filter(id=pk).delete()
        data = {
            "success": True,
            "xabar": "Bemor o'chirildi!"
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        bemor = Bemor.objects.get(id=pk)
        serializer = BemorSerializer(bemor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

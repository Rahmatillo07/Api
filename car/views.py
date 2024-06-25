from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializer




class CarApiView(APIView):
    def get(self,request:Request):
        cars = Car.objects.values()
        return Response({'cars':cars})

    def post(self,request:Request):
        cars = Car.objects.create(
            name=request.data['name'],
            color=request.data['color'],
            price=request.data['price'],
            description = request.data['description']
        )
        return Response(model_to_dict(cars))




























# class CarApiView(ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
# class CarDetailApiView(RetrieveAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer



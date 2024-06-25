from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

from .models import Car


car_object = Car(name='Nexia',color='qora',price=126,description='NexiaNexiaNexiaNexiaNexia')
class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=20)
    price = serializers.CharField()
    description = serializers.CharField()





def serialization():
    print(car_object)
    serializer = CarSerializer(car_object)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)


def deserialization():
    json = b'{"name":"Nexia","color":"qora","price":"126","description":"NexiaNexiaNexiaNexiaNexia"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    print(data)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
















# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = ['name','color','price','description']


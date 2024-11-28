from .models import *
from rest_framework import serializers

class userSerializers(serializers.ModelSerializer):
    Image = serializers.ImageField(required=False)


    class Meta:
        model = users
        fields = '__all__'


class adminSerializers(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = '__all__'


class bookserializers(serializers.ModelSerializer):
    Image = serializers.ImageField(use_url=True,required=False)


    class Meta:
        model = books
        fields = '__all__'


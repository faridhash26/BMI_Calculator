from django.shortcuts import get_object_or_404
from rest_framework import serializers
from decimal import Decimal

from .models import UserBmiInfo



class CreateBMIInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBmiInfo
        fields = ( 'age', 'weight', 'height')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['bmi'] =Decimal((validated_data.get("weight")/pow(validated_data.get("height"),2))* 10000)
        bmi_user_info = UserBmiInfo.objects.create(**validated_data)
        bmi_user_info.save()
        return bmi_user_info

class ResponseCreateBMIInfoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.name")
    difference= serializers.SerializerMethodField()
    class Meta:
        model = UserBmiInfo
        fields = ('user', 'age', 'weight', 'height' ,'bmi' , 'status' , 'difference')
    def get_difference(self, obj):
        if obj.bmi:
            bmi = round(obj.bmi ,1)
            if bmi <= 19 :
                normal_weight=(19*pow(obj.height,2)) /10000
                return round(normal_weight-obj.weight,1)
            if 19 < bmi <=25:
                return 0
            if 25 < bmi:
                normal_weight=(25*pow(obj.height,2)) /10000
                return round(obj.weight-normal_weight,1)
            return 0
            

                                    
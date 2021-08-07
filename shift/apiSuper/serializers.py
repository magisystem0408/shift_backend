from rest_framework import serializers
from ..models import ShiftBoard,Category


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model =ShiftBoard
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields ='__all__'
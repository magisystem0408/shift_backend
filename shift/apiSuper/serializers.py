from rest_framework import serializers
from ..models import ShiftBoard, Category
from django.contrib.auth.models import User


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self,validated_data):
        superuser =User.objects.create_superuser(**validated_data)
        return superuser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftBoard
        fields = '__all__'


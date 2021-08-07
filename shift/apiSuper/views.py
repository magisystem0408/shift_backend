from rest_framework import generics
from rest_framework import viewsets
from .serializers import ShiftSerializer, CategorySerializer
from ..models import Category, ShiftBoard

##一覧用
class ShiftListView(generics.ListAPIView):
    queryset = ShiftBoard.objects.all()
    serializer_class = ShiftSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

##詳細用
class ShiftDetailView(generics.RetrieveAPIView):
    queryset = ShiftBoard.objects.all()
    serializer_class = ShiftSerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

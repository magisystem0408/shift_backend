from rest_framework.permissions import AllowAny
from rest_framework import generics,viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ShiftSerializer, CategorySerializer,SuperUserSerializer
from ..models import Category, ShiftBoard

#ユーザー作成用
class CreateSuperUserView(generics.CreateAPIView):
    serializer_class =SuperUserSerializer
    permission_classes =(AllowAny,)


##一覧用
class ShiftListView(generics.ListAPIView):
    queryset = ShiftBoard.objects.all()
    serializer_class = ShiftSerializer

    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['category','count','date','release']

    permission_classes =(AllowAny,)




class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes =(AllowAny,)

##詳細用
class ShiftDetailView(generics.RetrieveAPIView):
    queryset = ShiftBoard.objects.all()
    serializer_class = ShiftSerializer
    permission_classes =(AllowAny,)


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes =(AllowAny,)


# 作成用
class ShiftViewSet(viewsets.ModelViewSet):
    queryset=ShiftBoard.objects.all()
    serializer_class =ShiftSerializer


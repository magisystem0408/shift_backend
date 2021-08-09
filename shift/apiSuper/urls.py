from django.urls import path
from django.conf.urls import include
from .views import ShiftListView,CategoryListView,ShiftDetailView,CategoryDetailView,CreateSuperUserView

urlpatterns =[

    path('list-shift',ShiftListView.as_view(),name='list-shift'),
    path('list-category',CategoryListView.as_view(),name='list-category'),

    path('detail-shift/<str:pk>/',ShiftDetailView().as_view(),name='detail-shift'),
    path('detail-category/<str:pk>/',CategoryDetailView.as_view(),name='detail-category'),

    path('register/',CreateSuperUserView.as_view(),name="register"),

    path('auth/',include('djoser.urls.jwt'))

]
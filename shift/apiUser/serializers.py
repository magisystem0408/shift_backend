from django.urls import path
from shift.api import views

urlpatterns =[
    path('list-shift/',ShiftList.as_view(),name='list-shift'),
]
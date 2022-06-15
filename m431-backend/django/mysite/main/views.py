from asyncio import events
from django.shortcuts import render
from main.models import Appreciation, Observation
from common.drf import CustomListAPIView, CustomPermission, CustomListCreateAPIView, CustomRetrieveUpdateDestroyAPIView
from rest_framework import serializers, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def home(request):
    return render(request, 'main/home.html', None)


class AppreciationList(CustomListCreateAPIView):
    """
    List all instances.
    """
    model = Appreciation
    fields = "__all__"
    search_fields = ('name',)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'appreciation')
    # permission_classes = [CustomPermission]

class AppreciationDetail(CustomRetrieveUpdateDestroyAPIView):
    """
    List all instances.
    """
    model = Appreciation
    fields = "__all__"
    # search_fields = ('name',)
    # permission_classes = [CustomPermission]

# class ScheduleList(CustomListAPIView):
#     """
#     List all instances.
#     """
#     model = Schedule
#     fields = "__all__"
#     search_fields = ('date',)
#     depth = 0
#     # permission_classes = [CustomPermission]




class ObservationList(CustomListCreateAPIView):
    """
    List all instances.
    """
    model = Observation
    fields = "__all__"


class ObservationDetail(CustomRetrieveUpdateDestroyAPIView):
    """
    List all instances.
    """
    model = Observation
    fields = "__all__"
from django.urls import path, include
from rest_framework import routers

from . import viewsets as core_viewsets

rest_router = routers.DefaultRouter()
rest_router.register(r'airplane', core_viewsets.AirplaneViewSet)

urlpatterns = [
    path('', include(rest_router.urls), name='airplane-api'),
]

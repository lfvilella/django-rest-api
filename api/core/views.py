from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ToolViewSet(viewsets.ModelViewSet):
    queryset = models.Tool.objects.all()
    serializer_class = serializers.ToolSerializer

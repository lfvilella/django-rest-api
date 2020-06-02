from rest_framework import serializers
from . import models


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tool
        fields = ['id', 'title', 'link', 'description']

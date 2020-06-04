from rest_framework import viewsets
from django.http import Http404
from . import models, serializers


class ToolViewSet(viewsets.ModelViewSet):
    queryset = models.Tool.objects.all()
    serializer_class = serializers.ToolSerializer

    def get_queryset(self):
        queryset = models.Tool.objects.all()
        query_params = self.request.query_params

        tags = query_params.getlist('tags', [])
        if tags:
            queryset = queryset.filter(tags__contains=tags)

        title = query_params.get('title', None)
        if title:
            queryset = queryset.filter(title=title)

        link = query_params.get('link', None)
        if link:
            queryset = queryset.filter(link=link)

        if not queryset.exists():
            raise Http404

        return queryset

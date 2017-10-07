from django.shortcuts import render

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from samples.models import Sample
from samples.serializers import SampleSerializer

import logging

class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.order_by('name')
    serializer_class = SampleSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        instance = serializer.save(dataset=self.request.dataset)

        return super(SampleViewSet, self).perform_create(serializer)


class DatasetSamplesViewSet(viewsets.ViewSet):
    queryset = Sample.objects.select_related('dataset').all()
    serializer_class = SampleSerializer

    def list(self, request, dataset_pk=None):
        queryset = self.queryset.filter(dataset=dataset_pk)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

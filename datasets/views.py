from rest_framework import permissions, viewsets
from rest_framework.response import Response

from datasets.models import Dataset
from datasets.serializers import DatasetSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.order_by('name')
    serializer_class = DatasetSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(DatasetViewSet, self).perform_create(serializer)


class AccountDatasetsViewSet(viewsets.ViewSet):
    queryset = Dataset.objects.select_related('author').all()
    serializer_class = DatasetSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
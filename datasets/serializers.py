from rest_framework import serializers

from authentication.serializers import AccountSerializer
from datasets.models import Dataset


class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset

        fields = ('id', 'name', 'description', 'size', 'precision', 'recall',\
            'specificity', 'fmeasure', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(DatasetSerializer, self).get_validation_exclusions()

        return exclusions
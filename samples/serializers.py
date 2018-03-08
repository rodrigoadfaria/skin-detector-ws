from rest_framework import serializers

from datasets.serializers import DatasetSerializer
from .models import Sample


class SampleSerializer(serializers.ModelSerializer):

    dataset = DatasetSerializer(read_only=True)

    class Meta:
        model = Sample

        fields = ('id', 'name', 'original_image', 'ground_truth_image', \
            'ground_truth_color_image', 'output_image', 'trapezia_image', \
            'metrics', 'dataset', 'created_at', 'updated_at')

        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(SampleSerializer, self).get_validation_exclusions()

        return exclusions
from rest_framework import serializers

from .models import Metric


class MetricSerializer(serializers.ModelSerializer):


    class Meta:
        model = Metric

        fields = ('id', 'method', 'precision', 'recall', 'specificity', \
            'fmeasure', 'dataset', 'created_at', 'updated_at')

        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(MetricSerializer, self).get_validation_exclusions()

        return exclusions
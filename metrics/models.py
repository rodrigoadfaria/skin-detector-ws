from django.db import models

from datasets.models import Dataset
from samples.models import Sample

class Metric(models.Model):

    method = models.TextField(max_length=40, blank=False)

    precision = models.FloatField()
    recall = models.FloatField()
    specificity = models.FloatField()
    fmeasure = models.FloatField()

    # the metric can belong to dataset or sample
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='metrics')
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='metrics')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.method)
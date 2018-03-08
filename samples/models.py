from django.db import models
from datasets.models import Dataset

class Sample(models.Model):

    name = models.TextField(max_length=200, blank=False)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)

    original_image = models.ImageField(null=False, blank=False)
    ground_truth_image = models.ImageField()
    ground_truth_color_image = models.ImageField()
    output_image = models.ImageField()
    trapezia_image = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.name)

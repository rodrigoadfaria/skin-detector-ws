from django.db import models

class Dataset(models.Model):

    name = models.TextField(max_length=140, blank=False)
    description = models.TextField()
    size = models.IntegerField()

    precision = models.FloatField()
    recall = models.FloatField()
    specificity = models.FloatField()
    fmeasure = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.name)

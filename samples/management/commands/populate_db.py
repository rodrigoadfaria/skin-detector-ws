from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datasets.models import Dataset
from samples.models import Sample

# so you can access settings.MEDIA_ROOT
from django.conf import settings

# so you can copy file to MEDIA_ROOT if need be
from shutil import copyfile

import os
from datetime import datetime
import pytz

class Command(BaseCommand):

    help = 'Adds datasets with their samples into MEDIA.'

    def add_arguments(self, parser):
        parser.add_argument('--ori', type=str, \
            help='Path to the original image')
        parser.add_argument('--gt', type=str, \
            help='Path to the ground truth image')
        parser.add_argument('--gtc', type=str, \
            help='Path to the ground truth colored image')
        parser.add_argument('--out', type=str, \
            help='Path to the output image')
        parser.add_argument('--tra', type=str, \
            help='Path to the trapezia image')

        parser.add_argument('--dataset_id', type=int, \
            help='Dataset id which this sample belongs to')

        parser.add_argument('--pr', type=float, \
            help='Precision metric computed by the used method')
        parser.add_argument('--re', type=float, \
            help='Recall metric computed by the used method')
        parser.add_argument('--sp', type=float, \
            help='Specificity metric computed by the used method')
        parser.add_argument('--fm', type=float, \
            help='F-measure metric computed by the used method')


    def handle(self, *args, **options):

        # the path of the file relative to media_source
        original_img = options['ori']
        gound_truth_img = options['gt']
        gound_truth_color_img = options['gtc']
        output_img = options['out']
        trapezia_img = options['tra']

        precision = options['pr']
        recall = options['re']
        specificity = options['sp']
        fmeasure = options['fm']
        dataset_id = options['dataset_id']

        # copy file to media root folder
        # TODO: change the path of the file to be kept to this one within media root
        media_target = os.path.realpath(settings.MEDIA_ROOT)
        #copyfile(original_img, media_target)

        base = os.path.basename(original_img)
        title = os.path.splitext(base)[0]

        dataset = Dataset.objects.get(id=dataset_id)
        p = Sample(dataset=dataset, name=title, \
                original_image=original_img, \
                ground_truth_image=gound_truth_img, \
                ground_truth_binary_image=gound_truth_color_img, \
                output_image=output_img, \
                trapezia_image=trapezia_img, \
                precision=precision, recall=recall, \
                specificity=specificity, fmeasure=fmeasure)
        p.save()
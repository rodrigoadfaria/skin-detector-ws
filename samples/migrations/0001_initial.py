# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datasets', '0002_auto_20170809_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('original_image', models.ImageField(upload_to='')),
                ('ground_truth_image', models.ImageField(upload_to='')),
                ('ground_truth_binary_image', models.ImageField(upload_to='')),
                ('output_image', models.ImageField(upload_to='')),
                ('trapezia_image', models.ImageField(upload_to='')),
                ('precision', models.FloatField()),
                ('recall', models.FloatField()),
                ('specificity', models.FloatField()),
                ('fmeasure', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset')),
            ],
        ),
    ]

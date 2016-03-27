# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-27 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150)),
                ('publisher', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price_in_dollars', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]

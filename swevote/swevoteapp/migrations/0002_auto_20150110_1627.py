# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import swevoteapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('swevoteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_pic',
            field=models.ImageField(upload_to=swevoteapp.models.generate_filename, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swevoteapp', '0003_auto_20150110_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='is_current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

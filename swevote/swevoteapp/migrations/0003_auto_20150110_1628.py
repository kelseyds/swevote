# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('swevoteapp', '0002_auto_20150110_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='users_have_voted_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
    ]

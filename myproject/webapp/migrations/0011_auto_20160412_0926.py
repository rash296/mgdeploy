# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20160412_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test_avg',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_no',
        ),
    ]

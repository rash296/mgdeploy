# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_avg',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='test_no',
            field=models.IntegerField(null=True),
        ),
    ]

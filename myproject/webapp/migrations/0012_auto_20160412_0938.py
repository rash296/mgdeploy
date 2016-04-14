# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20160412_0926'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testrecord',
            unique_together=set([]),
        ),
    ]

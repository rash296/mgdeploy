# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_testrecord_test_avg'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentsheet', models.FileField(upload_to='student/%Y/%m/%d')),
            ],
        ),
    ]

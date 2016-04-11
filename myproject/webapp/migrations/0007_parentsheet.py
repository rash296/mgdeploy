# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_studentsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parentsheet', models.FileField(upload_to='parent/%Y/%m/%d')),
            ],
        ),
    ]

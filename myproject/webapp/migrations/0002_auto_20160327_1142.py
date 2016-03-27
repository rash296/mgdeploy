# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendancerecord',
            unique_together=set([('stud_ID', 'attendance_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='testrecord',
            unique_together=set([('stud_ID', 'test_no')]),
        ),
    ]

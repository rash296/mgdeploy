# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendancesheet', models.FileField(upload_to='attendance/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stud_ID', models.IntegerField(null=True)),
                ('stud_name', models.CharField(max_length=30, null=True)),
                ('stud_presence', models.IntegerField(null=True)),
                ('attendance_no', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to='documents/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testsheet', models.FileField(upload_to='test/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stud_ID', models.IntegerField(null=True)),
                ('stud_name', models.CharField(max_length=30, null=True)),
                ('stud_score', models.IntegerField(null=True)),
                ('test_no', models.IntegerField(null=True)),
            ],
        ),
    ]

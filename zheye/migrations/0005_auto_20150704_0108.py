# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zheye', '0004_auto_20150704_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='personanswership',
            name='question',
            field=models.ForeignKey(blank=True, to='zheye.Question', null=True),
        ),
        migrations.AlterField(
            model_name='personanswership',
            name='answer',
            field=models.ForeignKey(to='zheye.Answer', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zheye', '0002_auto_20150703_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='vote_up',
            field=models.IntegerField(default=0, verbose_name='\u8d5e\u6210'),
        ),
    ]

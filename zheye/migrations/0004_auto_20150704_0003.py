# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zheye', '0003_answer_vote_up'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personanswership',
            options={'ordering': ['update_time']},
        ),
        migrations.AlterField(
            model_name='personanswership',
            name='PAShip',
            field=models.CharField(max_length=20, choices=[(b'write', b'\xe5\x9b\x9e\xe7\xad\x94'), (b'vote', b'\xe8\xb5\x9e\xe5\x90\x8c'), (b'collect', b'\xe6\x94\xb6\xe8\x97\x8f'), (b'focus', b'\xe5\x85\xb3\xe6\xb3\xa8')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('zheye', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='vote_down_persons',
            field=models.ManyToManyField(related_name='answers_the_person_down', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='vote_up_persons',
            field=models.ManyToManyField(related_name='answers_the_person_up', through='zheye.PersonAnswerShip', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='collect_answers',
            field=models.ManyToManyField(related_name='persons_collect_the_answer', to='zheye.Answer', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='fans',
            field=models.ManyToManyField(related_name='stars', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='focus_questions',
            field=models.ManyToManyField(related_name='persons_focus_the_question', to='zheye.Question', blank=True),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='from_person',
            field=models.ForeignKey(related_name='messages_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='to_person',
            field=models.ForeignKey(related_name='messages_to', to=settings.AUTH_USER_MODEL),
        ),
    ]

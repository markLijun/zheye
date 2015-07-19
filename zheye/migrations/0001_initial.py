# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(default=20, verbose_name='\u5e74\u9f84')),
                ('intro_short', models.TextField(verbose_name='\u4e00\u53e5\u8bdd\u4ecb\u7ecd')),
                ('intro_long', models.TextField(verbose_name='\u81ea\u6211\u4ecb\u7ecd')),
                ('gender', models.CharField(max_length=20, verbose_name='\u6027\u522b', choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(verbose_name='\u56de\u7b54')),
                ('answer_time', models.DateTimeField(auto_now_add=True, verbose_name='\u56de\u7b54\u65f6\u95f4')),
                ('vote_down', models.IntegerField(default=0, verbose_name='\u53cd\u5bf9')),
                ('author', models.ForeignKey(related_name='answers_write', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_reply', models.TextField(verbose_name='\u56de\u7b54\u8bc4\u8bba')),
                ('reply_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('answer', models.ForeignKey(related_name='answer_replys_in_the_answer', to='zheye.Answer')),
                ('author', models.ForeignKey(related_name='answer_replys_write', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerReReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_re_reply', models.TextField()),
                ('rereply_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('answer', models.ForeignKey(related_name='answer_re_replys_in_the_answer', to='zheye.Answer')),
                ('answer_reply', models.ForeignKey(related_name='answer_re_replys_in_the_answer_reply', to='zheye.AnswerReply')),
                ('author', models.ForeignKey(related_name='answer_re_replys_write', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonAnswerShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PAShip', models.CharField(max_length=20, choices=[(b'write', b'write'), (b'vote', b'vote')])),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer', models.ForeignKey(to='zheye.Answer')),
                ('person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(verbose_name='\u79c1\u4fe1')),
                ('message_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4')),
                ('from_person', models.ForeignKey(related_name='messages_from', blank=True, to=settings.AUTH_USER_MODEL)),
                ('to_person', models.ForeignKey(related_name='messages_to', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_short', models.TextField(verbose_name='\u95ee\u9898')),
                ('question_long', models.TextField(verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('question_time', models.DateTimeField(auto_now_add=True, verbose_name='\u95ee\u9898\u65f6\u95f4')),
                ('author', models.ForeignKey(related_name='questions_raise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sortion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sortion', models.CharField(max_length=200, verbose_name='\u5206\u7c7b')),
                ('good_persons', models.ManyToManyField(related_name='sortions_good', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='sortion',
            field=models.ForeignKey(related_name='questions_in_the_sortion', to='zheye.Sortion'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers_in_the_question', to='zheye.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='vote_down_persons',
            field=models.ManyToManyField(related_name='answers_the_person_down', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='vote_up_persons',
            field=models.ManyToManyField(related_name='answers_the_person_up', through='zheye.PersonAnswerShip', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='collect_answers',
            field=models.ManyToManyField(related_name='persons_collect_the_answer', to='zheye.Answer'),
        ),
        migrations.AddField(
            model_name='person',
            name='fans',
            field=models.ManyToManyField(related_name='stars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='focus_questions',
            field=models.ManyToManyField(related_name='persons_focus_the_question', to='zheye.Question'),
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='person',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]

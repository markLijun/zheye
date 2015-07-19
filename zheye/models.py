# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser,User

import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')   
    
class Person(AbstractUser):
    GENDERS = (
        ('male','男'),
        ('female','女'),
    )
    age=models.IntegerField(u'年龄',default=20)
    intro_short=models.TextField(u'一句话介绍')
    intro_long=models.TextField(u'自我介绍')
    gender=models.CharField(u'性别',max_length=20,choices=GENDERS)
    fans=models.ManyToManyField('self',symmetrical=False,related_name="stars",blank=True)
    focus_questions=models.ManyToManyField('Question',related_name='persons_focus_the_question',blank=True)
    collect_answers=models.ManyToManyField('Answer',related_name='persons_collect_the_answer',blank=True)
     
    def __unicode__(self):
        return self.username
        
class PrivateMessage(models.Model):
    
    from_person=models.ForeignKey(Person,related_name='messages_from')
    to_person=models.ForeignKey(Person,related_name='messages_to')
    message=models.TextField(u'私信')
    message_time=models.DateTimeField(u'发送时间',auto_now_add=True)
    
    def __unicode__(self):
        return self.message
    
    
class Sortion(models.Model):
    good_persons=models.ManyToManyField(Person,related_name="sortions_good")
    sortion=models.CharField(u'分类',max_length=200)
    
    def __unicode__(self):
        return self.sortion
        
class Question(models.Model):
    author=models.ForeignKey(Person,related_name="questions_raise")
    sortion=models.ForeignKey(Sortion,related_name="questions_in_the_sortion")
    question_short=models.TextField(u'问题')
    question_long=models.TextField(u'问题描述')
    question_time=models.DateTimeField(u'问题时间',auto_now_add=True)
    
    def __unicode__(self):
        return self.question_short
        
class Answer(models.Model):
    author=models.ForeignKey(Person,related_name="answers_write")
    question=models.ForeignKey(Question,related_name="answers_in_the_question")
    answer=models.TextField(u'回答')
    answer_time=models.DateTimeField(u'回答时间',auto_now_add=True)
    vote_up=models.IntegerField(u'赞成',default=0)
    vote_down=models.IntegerField(u'反对',default=0)
    vote_up_persons=models.ManyToManyField(Person,related_name="answers_the_person_up",through='PersonAnswerShip',blank=True)
    vote_down_persons=models.ManyToManyField(Person,related_name="answers_the_person_down",blank=True)
    
    def get_vote_last(self):
        return self.vote_up-self.vote_down
            
    def __unicode__(self):
        return self.answer
        
class PersonAnswerShip(models.Model):
    AnswerShip = (
        ('write','回答'),
        ('vote','赞同'),
        ('collect','收藏'),
        ('focus','关注'),
        ('raise','提出'),
    )
    person=models.ForeignKey(Person)
    answer=models.ForeignKey(Answer,blank=True,null=True)
    question=models.ForeignKey(Question,blank=True,null=True)
    PAShip=models.CharField(max_length=20,choices=AnswerShip)
    update_time=models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering=['update_time']
    def __unicode__(self):
        return self.PAShip
        
class AnswerReply(models.Model):
    author=models.ForeignKey(Person,related_name="answer_replys_write")
    answer=models.ForeignKey(Answer,related_name="answer_replys_in_the_answer")
    answer_reply=models.TextField(u'回答评论')
    reply_time=models.DateTimeField(u'评论时间',auto_now_add=True)
    
    def __unicode__(self):
        return self.answer_reply
        
class AnswerReReply(models.Model):
    author=models.ForeignKey(Person,related_name="answer_re_replys_write")
    answer=models.ForeignKey(Answer,related_name="answer_re_replys_in_the_answer")
    answer_reply=models.ForeignKey(AnswerReply,related_name="answer_re_replys_in_the_answer_reply")
    answer_re_reply=models.TextField()
    rereply_time=models.DateTimeField(u'评论时间',auto_now_add=True)
    
    def __unicode__(self):
        return self.answer_re_reply
        
      
        
    
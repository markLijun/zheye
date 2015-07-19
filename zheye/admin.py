from django.contrib import admin
from zheye.models import Person,Sortion,Question,Answer,AnswerReply,AnswerReReply,PrivateMessage,PersonAnswerShip

# Register your models here.
admin.site.register(Person)
admin.site.register(Sortion)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerReply)
admin.site.register(AnswerReReply)
admin.site.register(PrivateMessage)
admin.site.register(PersonAnswerShip)

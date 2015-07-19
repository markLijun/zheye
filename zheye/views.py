#coding=utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from zheye.models import Person,Sortion,Question,Answer,AnswerReply,AnswerReReply,PersonAnswerShip
from django.forms import ModelForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields=("username","password","email","gender","age","intro_short","intro_long")
        
def test(request):
    text=request.GET['sortion']
    sortions=Sortion.objects.filter(sortion__icontains=text)[:5]
    html='<ul class="list-unstyled tips" id="tipsul">'
    for sortion in sortions:
        html=html+'<li style="cursor:default">'+sortion.sortion+'</li>'
    html=html+'</ul>'
    return HttpResponse(html)

def index(request):
    questions = Question.objects.all()
    if request.user.is_authenticated():
        stars=request.user.stars.all()
        ships=PersonAnswerShip.objects.filter(person=stars)
        return render(request, 'zheye/index.html',{'ships':ships,})
    else:
        ships=PersonAnswerShip.objects.all()
        return render(request, 'zheye/index.html',{'ships':ships,})
    
def login_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else: 
            return HttpResponse("没激活！")
    else:
        return HttpResponse("没有这个用户！")
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def register(request):
    if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                person=Person()
                person.username = form.cleaned_data['username']
                person.intro_short = form.cleaned_data['intro_short']
                person.intro_long = form.cleaned_data['intro_long']
                person.age = form.cleaned_data['age']
                person.gender = request.POST['gender']
                person.set_password(form.cleaned_data['password'])
                person.email = form.cleaned_data['email']
                person.save()                
                person.fans.add(person)
                person.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return HttpResponse("NO")
    else:
        form = PersonForm()
        return render(request, 'zheye/register.html', {'form': form})
        
def add_question(request):
    if request.method == 'POST':
        select_sortion=Sortion.objects.get(sortion=request.POST['hidden_sortion'])
        the_question=Question.objects.create(author=request.user,sortion=select_sortion,question_short=request.POST['question_short'],question_long=request.POST['question_long'])
        PersonAnswerShip.objects.create(person=request.user,question=the_question,PAShip='raise')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/index/')
def show_question(request,question_id):
    question=Question.objects.get(id=question_id)
    answers=Answer.objects.filter(question=question)
    return render(request, 'zheye/show_question.html', {'answers': answers,'question':question})

def ajax_reply(request):
    answer_id=request.GET['answer_id']
    answer=Answer.objects.get(id=answer_id)
    replys=answer.answer_replys_in_the_answer.all()
    html='<div style="border:1px solid #eee;width:70%"><ul class="list-unstyled replys">'
    for reply in replys:
        html=html+'<li style="cursor:default">'+reply.answer_reply+'</li>'
    html=html+'</ul><textarea id="add_reply" class="form-control" rows="2" name="add_reply"></textarea><button type="submit" class="btn btn-primary add_reply_button" style="float:right">评论</button><div class="clearfix"></div>'
    return HttpResponse(html)
    
def add_reply(request):
    answer_id=request.GET['sss']
    reply_text=request.GET['reply_text']
    answer=Answer.objects.get(id=answer_id)
    AnswerReply.objects.create(author=request.user,answer=answer,answer_reply=reply_text)
    return HttpResponse("nihao")
    
@login_required(login_url='/index/')
def focus(request):
    question_id=request.GET['question_id']
    question=Question.objects.get(id=question_id)
    ships=PersonAnswerShip.objects.filter(person=request.user,question=question,PAShip='focus')
    if ships:
        PersonAnswerShip.objects.filter(person=request.user,question=question,PAShip='focus').delete()
        return HttpResponse("yes")
    else:
        PersonAnswerShip.objects.create(person=request.user,question=question,PAShip='focus')
        return HttpResponse("no")
    
def collect(request):
    answer_id=request.GET['answer_id']
    answer=Answer.objects.get(id=answer_id)
    ships=PersonAnswerShip.objects.filter(person=request.user,answer=answer,PAShip='collect')
    if ships:
        PersonAnswerShip.objects.filter(person=request.user,answer=answer,PAShip='collect').delete()
        return HttpResponse("yes")
    else:
        PersonAnswerShip.objects.create(person=request.user,answer=answer,PAShip='collect')
        return HttpResponse("no")
        
def add_answer(request):
    answer_text=request.POST['answer_text']
    question_id=request.POST['hidden']
    question=Question.objects.get(id=question_id)
    Answer.objects.create(author=request.user,question=question,answer=answer_text)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def vote_up(request):
    answer_id=request.GET['answer_id']
    answer=Answer.objects.get(id=answer_id)
    answer.vote_up+=1
    answer.save()
    PersonAnswerShip.objects.create(person=request.user,answer=answer,PAShip='vote')
    answer.vote_up_persons.add(request.user)
    return HttpResponse(answer.vote_up)
    
def vote_down(request):
    answer_id=request.GET['answer_id']
    answer=Answer.objects.get(id=answer_id)
    answer.vote_down+=1
    answer.save()
    answer.vote_down_persons.add(request.user)
    return HttpResponse(answer.vote_down)
    
    

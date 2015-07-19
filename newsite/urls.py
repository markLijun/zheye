"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from zheye import views
from newsite import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name="index"),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login_view,name='login'),
    url(r'^test/',views.test,name='test'),
    url(r'^ajax_reply/',views.ajax_reply,name='ajax_reply'),
    url(r'^logout/',views.logout_view,name='logout'),
    url(r'^focus/',views.focus,name='focus'),
    url(r'^vote_up/',views.vote_up,name='vote_up'),
    url(r'^vote_down/',views.vote_down,name='vote_down'),
    url(r'^question/(?P<question_id>[0-9]+)/$',views.show_question,name='show_question'),
    url(r'^collect/',views.collect,name='collect'),
    url(r'^add_question/',views.add_question,name='add_question'),
    url(r'^add_answer/',views.add_answer,name='add_answer'),
    url(r'^add_reply/',views.add_reply,name='add_reply'),
    url(r'^', include('django.contrib.auth.urls')),
]


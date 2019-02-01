#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import RequestContext
from common_db import *
#from action_request import user_regist
import random


def is_login(request):
        return request.session.get('user_name',None)



def login(request):
    user_name=is_login(request)
    if request.session.get('login', None):
        return render_to_response('user_login.html',{"user_name":user_name})
    return render_to_response('user_login.html',{"user_name":user_name})

def regist(request):
    user_name=is_login(request)
    if request.session.get('login', None):
        return render_to_response('user_regist.html',{"user_name":user_name})
    return render_to_response('user_regist.html',{"user_name":user_name})


def index(request):
    user_name=is_login(request)
    return render_to_response('index.html',{"user_name":user_name})

def test(request):
    user_name=is_login(request)
    return render_to_response('test.html',{"user_name":user_name})

def test_question(request):
    user_name=is_login(request)
    return render_to_response('test_question.html',{"user_name":user_name})

def activity(request):
    user_name=is_login(request)
    return render_to_response('activity.html',{"user_name":user_name})

def activity_detail(request):
    user_name=is_login(request)
    return render_to_response('activity_detail.html',{"user_name":user_name})

def classes(request):
    user_name=is_login(request)
    return render_to_response('classes.html',{"user_name":user_name})

def class_detail(request):
    user_name=is_login(request)
    return render_to_response('class_detail.html',{"user_name":user_name})

def discuss(request):
    user_name=is_login(request)
    return render_to_response('discuss.html',{"user_name":user_name})
def discuss_add(request):
    user_name=is_login(request)
    return render_to_response('discuss_add.html',{"user_name":user_name})
def discuss_detail(request):
    user_name=is_login(request)
    return render_to_response('discuss_detail.html',{"user_name":user_name})

def download(request):
    user_name=is_login(request)
    return render_to_response('download.html',{"user_name":user_name})


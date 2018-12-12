#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import RequestContext
from common_db import *
from action_request import *





def user_login(request):

                return render_to_response('user_login.html',{})


def user_regist(request):

                return render_to_response('user_login.html',{})




def index(request):


                return render_to_response('index.html',{'test':"Hello, world. You're at the polls index."})

def test(request):
                return render_to_response('test.html',{'test':"Hello, world. You're at the polls index."})
def test_question(request):
                return render_to_response('test_question.html',{'test':"Hello, world. You're at the polls index."})

def activity(request):
                return render_to_response('activity.html',{'test':"Hello, world. You're at the polls index."})

def activity_detail(request):
                return render_to_response('activity_detail.html',{'test':"Hello, world. You're at the polls index."})


def classes(request):
                return render_to_response('classes.html',{'test':"Hello, world. You're at the polls index."})


def class_detail(request):
                return render_to_response('class_detail.html',{'test':"Hello, world. You're at the polls index."})

def discuss(request):
                return render_to_response('discuss.html',{'test':"Hello, world. You're at the polls index."})
def discuss_add(request):
                return render_to_response('discuss_add.html',{'test':"Hello, world. You're at the polls index."})
def discuss_detail(request):
                return render_to_response('discuss_detail.html',{'test':"Hello, world. You're at the polls index."})

def download(request):
                return render_to_response('download.html',{'test':"Hello, world. You're at the polls index."})


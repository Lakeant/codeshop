#coding:utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from common_db import custom_sql,single_column_sql,excute_sql
from django.contrib.auth.hashers import make_password, check_password
from send_mail import  send_mail
from django.shortcuts import render_to_response
from django.core.cache import cache
import random


import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@csrf_exempt
def user_regist(request):
    result={}
    if request.method=="POST":
        username=request.POST.get('user_str')
        phone=request.POST.get('phone_str')
        email=request.POST.get('email_str')
        pwd=request.POST.get('password_str')
        user_exist_flag=single_column_sql("select count(1)  as flag from users where user_name='{0}'".format(username))
        user_phone_username=single_column_sql("select left(user_name,4)   as flag from users where mobile='{0}'".format(phone))
        user_email_username=single_column_sql("select left(user_name,4)  as flag from users where email='{0}'".format(email))
         #用户已存在
        if user_exist_flag[0] >= 1:
            result['error']='用户名已注册过！'
            result['valid']=-1
            return HttpResponse(json.dumps(result))
         #用户已存在
        if user_phone_username is not None:
            result['error']='邮箱已注册过！'
            result['valid']=-1
            return HttpResponse(json.dumps(result))
        #用户不存在，切没有用电话和邮箱注册过and user_phone_username is not None
        if user_exist_flag[0]==0  and user_email_username is  None:
            result['username']=username
            result['valid']=1
            result['error']='成功注册'
            excute_sql("insert into user(user_name,email,mobile,passwords) values('{username}','{email}','{mobile}','{password}')".format(username=username,email=email,mobile=phone,password=make_password(pwd)))
            result['error']='成功注册'
        else:
            result['username']=username
            result['valid']=0
            result['error']='其他错误，请重试！'
    else:
        result['valid']=0
        result['error']='非法请求，注册失败!'

    return HttpResponse(json.dumps(result))



@csrf_exempt
def mail_code(request):
    result={}
    if request.method=="POST":
        mail=request.POST.get('email_str')
        letters='12345667890'
        code=''.join(random.choice(letters) for x in range(4))
        if cache.get(mail):
            cache.delete(mail)
        cache.set(mail,code,300)
        title="【codeshop】收到新的验证码:"+code
        html='''
        欢迎加入【codeshop】！

        您的验证码为：{} （请确保是本人操作，否则请忽略）
                                        ---codeshop
        (这是一封自动产生的email，请勿回复。)
        '''.format(code)
        mess=send_mail(html,title,mail)
        result['status']=mess['status']
        result['mess']=mess['info']
    else:
        result['status']=0
        result['mess']="Not post!"

    return HttpResponse(json.dumps(result))

@csrf_exempt
def user_login(request):
    result={}
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        email_exist=single_column_sql("select count(1)  as flag from users where email='{0}'".format(email))
        if email_exist >0:
            user_=custom_sql("select passwords,user_name   from users where email='{0}'".format(email))
            print(user_[0]['passwords'])
            print(password)
            print(make_password(password))
            pass_valid=check_password(password,user_[0]['passwords'])
            if pass_valid:
                request.session.set_expiry(3600)
                request.session['login']=1
                request.session['user_name']=user_[0]['user_name']
                request.session['email']=email
                result['valid']=1
                result['mess']='登陆成功'
            else:
                result['valid']=0
                result['mess']='用户或者密码错误，请重试'
        else:
            result['valid']=0
            result['mess']='用户或者密码错误，请重试'
    else:
        result['valid']=0
        result['mess']='错误的请求信息'
    print(result)

    return  HttpResponse(json.dumps(result))

@csrf_exempt
def user_login_out(request):
    del request.session['login']
    del request.session['user_name']
    del request.session['email']
    return    render_to_response('index.html',{"user_name":'None'})

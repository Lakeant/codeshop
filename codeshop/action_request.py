#coding:utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from common_db import custom_sql,single_column_sql,excute_sql
from django.contrib.auth.hashers import make_password, check_password

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
        user_exist_flag=single_column_sql("select 1  as flag from users where user_name='{0}'".format(username))
        user_phone_username=single_column_sql("select left(user_name,4)   as flag from users where mobile='{0}'".format(phone))
        user_email_username=single_column_sql("select left(user_name,4)  as flag from users where email='{0}'".format(email))

        #用户不存在，切没有用电话和邮箱注册过
        if user_exist_flag is None and user_phone_username is not None and user_email_username is not None:
            result['username']=username
            result['valid']=1
            result['error']='success !'
            excute_sql("insert into user(user_name,email,mobile,password) values('{username}','{email}','{mobile}','{password}')".format(username=username,email=email,mobile=phone,password=make_password(pwd)))
        else:
            result['username']=username
            result['valid']=0
            result['error']='unkown error !'
                    #用户已存在
        if user_exist_flag==1:
            result['error']='user exsist'
            result['valid']=-1
        #电话号码已存在
        if user_phone_username is not None:
            result['error']='user already has phone !'
            result['valid']=-2
        #邮箱已存在
        if user_email_username is not None:
            result['error']='user already has email !'
            result['valid']=-3
    else:
        result['username']=username
        result['valid']=0
        result['error']='user regist fail !not post!'

    return HttpResponse(json.dumps(result))



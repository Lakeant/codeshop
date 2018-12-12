#coding:utf-8
from django.http import HttpResponse

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def user_regist(request):
	result={}
	if request.method="POST":
		username=request.POST.get('user_str')
		pwd=request.POST.get('password_str')
		phone=request.POST.get('phone_str')
		print(username+"-"+pwd+"-"+phone)
		result['username']=username
		result['valid']=1
	else:
		result['username']=username
		result['valid']=0
		result['error']='ע��ʧ��'

	return HttpResponse('hello :'+username,content_type='application/json;charset=utf-8')



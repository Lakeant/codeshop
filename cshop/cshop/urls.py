"""cshop URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
from codeshop import views#,actions
#from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^activity/$', views.activity, name='activity'),
	url(r'^activity_detail/$', views.activity_detail, name='activity_detail$'),
	url(r'^classes/$', views.classes, name='classes$'),
	url(r'^class_detail/$', views.class_detail, name='class_detail$'),
	url(r'^discuss/$', views.discuss, name='discuss'),
	url(r'^discuss_detail/$', views.discuss_detail, name='discuss_detail$'),
	url(r'^discuss_add/$', views.discuss_add, name='discuss_add'),
	url(r'^download/$', views.download, name='download'),
	url(r'^test/$', views.test, name='test'),
	url(r'^test_question/$', views.test_question, name='test_question'),
	url(r'^user_regist/$', views.user_regist, name='user_regist'),
]
# urlpatterns += patterns('',
#      url(r'^codeshop/',include('codeshop.urls')),
#  )
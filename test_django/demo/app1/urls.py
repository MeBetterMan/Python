from django.contrib import admin
from django.urls import path, re_path
from app1 import views

# path不可以正则 re_path可以；（）里面的赋值给detail视图的形参
urlpatterns = [
    re_path('^$', views.index),

    # 测试模型类
    re_path(r'^(\d+)/$', views.detail, name='index'),
    re_path(r'^grades/$', views.grades),
    re_path(r'^students/$', views.students),
    re_path(r'^grades/(\d+)$', views.grades2Students),
    re_path(r'^addstudent/$', views.addstudent),
    re_path(r'^attribute/$', views.attribute),  # 学习request的属性
    re_path(r'^get1/$', views.get1),  # 学习request.GET属性
    re_path('^showRegister/$', views.showRegister),

    # 查看 HTTPResponse HTTPRequest的属性
    re_path('^showRegister/register/$', views.register),
    re_path('^showResponse/$', views.showResponse),

    # 测试cookie
    re_path('cookieTest/', views.cookieTest),  # 最后如果没有斜线 会找不到


    # 测试重定向
    re_path('redirect1/', views.redirect1),
    re_path('redirect2/', views.redirect2),

    # 测试session
    re_path(r'main/$', views.main_page),
    re_path(r'login/$', views.login),
    re_path(r'showMain/$', views.showMain),
    re_path(r'quit/$', views.quit),

    # 测试传给模板对象
    re_path(r'testObj/$', views.testObj),

    # 测试模板标签
    re_path(r'index_template/$',views.index_template),

    # 测试反向解析
    re_path(r'^good/(\d+)/$', views.good, name='good'),

    # 测试模板继承
    re_path(r'^child/$', views.child),

    # 获取验证码
    re_path(r'^verifycode/$', views.verifyCode),
    re_path(r'^verifycodefile/$', views.verifyCodefile),
    re_path(r'^verifycodecheck/$', views.verifycodecheck),

    # 上传文件
    re_path(r'^upfile/$', views.upfile),
    re_path(r'^savefile/$', views.savefile),

    # 分页
    re_path(r'^stuPage/(\d+)/$', views.stuPage),

    # ajax
    re_path(r'^ajaxStudent/$', views.ajaxStudent),
    re_path(r'^studentsinfo/$', views.studentsinfo),

    # 富文本
    re_path(r'^edit/$', views.edit),

    # celery
    re_path(r'^celery/$', views.celery),
]

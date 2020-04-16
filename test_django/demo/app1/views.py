from django.shortcuts import render
from .models import Grades, Students
# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("success")
    return render(request, 'app1/index.html')


def detail(request, num):
    return HttpResponse('detail-%s' % num)


def grades(requests):
    # 去模板取数据
    gradesList = Grades.objects.all()

    # 将数据传给模板，模板渲染页面，将渲染好页面返回给浏览器
    return render(requests, 'app1/grades.html', {"grades": gradesList})


def students(requests):
    # 去模板取数据
    studentList = Students.stuObj.all()

    # 将数据传给模板，模板渲染页面，将渲染好页面返回给浏览器
    return render(requests, 'app1/students.html', {"students": studentList})


def grades2Students(requets, grade_id):
    # 获得班级对象；pk 即id;
    grade = Grades.objects.get(pk=grade_id)
    # 获得班级下的所有学生；知道班级对象，可以直接查出以其为外键的所有对象
    studentsList = grade.student_set.all()
    return render(requets, 'app1/students.html', {'students': studentsList})


def addstudent(requets):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("mayun", 22, 0, grade, "我是马云")
    stu.save()
    return HttpResponse("student save")


def attribute(request):
    print(request.path)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse('success')


def get1(request):
    print(request.GET.get('a'))
    return HttpResponse('success')


def showRegister(request):
    return render(request, 'app1/register.html')


def register(request):
    print("register")
    name = request.POST.get("name")
    print(name)
    gender = request.POST.get("gender")
    print(gender)
    age = request.POST.get("age")
    print(age)
    hobby = request.POST.getlist("hobby")
    print(hobby)
    return HttpResponse(name + " " + gender + " " + age + " ")


def showResponse(request):
    rsp = HttpResponse()
    rsp.content = b'text respone '
    print(rsp.content)
    print(rsp.charset)
    print(rsp.status_code)
    return rsp


# cookie
def cookieTest(request):
    rsp = HttpResponse('test cookie')
    # 第一次调用服务器时cookie存入
    # rsp.set_cookie('fang', '33333')
    # 下一次可以读取cookie
    cookie = request.COOKIES['fang']
    rsp.write('<h1>' + cookie + '</h1>')
    return rsp


from django.http import HttpResponseRedirect
from django.shortcuts import redirect


# 重定向
def redirect1(request):
    return redirect('/app1/redirect2')


def redirect2(request):
    return HttpResponse("重定向页面")


# session
def main_page(request):
    # 取session
    username = request.session.get('name', '游客')
    print(username)
    return render(request, 'app1/main.html', {"username": username})


def login(request):
    return render(request, 'app1/login.html')


def showMain(request):
    name = request.POST.get("name")
    # 存储session
    request.session['name'] = name
    request.session.set_expiry(300)
    return redirect('app1/main')


from django.contrib.auth import logout


def quit(request):
    # request.session.clear()
    logout(request)  # 退出当前用户;三种方法都能用，推荐使用logout
    # request.session.flush()
    return redirect('app1/main/')


from app1.models import Students


# 传入对象
def testObj(request):
    stu = Students.stuObj.get(pk=1)
    return render(request, 'app1/testObj.html', {"stu": stu})


# 测试模板
def index_template(request):
    # 测试传对象
    stu = Students.stuObj.get(pk=1)
    # 测试if
    num = 10
    # 测试for
    studentList = Students.stuObj.all()
    return render(request, 'app1/index.html', {"stu": stu, "num": num, "stuList": studentList, "str": 'fang upper',
                                               'strList': ['fang', 'test', 'guolv']})


# 测试方向解析
def good(request, p1):
    return render(request, 'app1/good.html', {"num": p1, "str": "<h1>helo</h1>"})


def child(req):
    return render(req, 'app1/child.html')


from app1.VerifyCodeClass import verifyCode as ve


def verifyCode(req):
    return ve(req)


def verifyCodefile(req):
    f = req.session.get('flag', True)
    req.session.clear()
    str = ''
    if f is False:
        str = "请重新输入"
    return render(req, 'app1/verifycodefile.html', {"flag": str})


def verifycodecheck(req):
    sessionCode = req.session.get('verifycode').upper()
    formCode = req.POST.get('verifycode').upper()
    if sessionCode == formCode:
        return render(req, 'app1/verifysucess.html')
    else:
        req.session['flag'] = False
        return redirect('/verifycodefile/')


#引入settings.py配置文件
import  os
from django.conf import settings
def savefile(req):
    if req.method == "POST":
        pass
    else:
        return HttpResponse('上传失败')
    file = req.FILES['file']
    filePath = os.path.join(settings.MDEIA_ROOT, file.name)
    with open(filePath, 'wb') as fp:
        for info in file.chunks():# 将数据分成一段段
            fp.write(info)
    return HttpResponse('上传成功')


def upfile(req):
    return render(req,'app1/upfile.html')

from django.core.paginator import Page,Paginator
def stuPage(req, num):
    allList = Students.stuObj.all()
    stuList = Paginator(allList,2).page(int(num))
    return render(req, 'app1/stuPage.html',{"stuList":stuList})


def ajaxStudent(req):
    return render(req, 'app1/ajaxStudent.html')

from django.http import JsonResponse
def studentsinfo(req):
    stu = Students.stuObj.all()
    list = []
    for s in stu:
        list.append([s.sname, s.sage])
    return JsonResponse({"data": list})


def edit(req):
    return render(req, 'app1/edit.html')


import time
from celery import task
def celery(req):


    return render(req, 'app1/celery.html')
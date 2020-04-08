import base64
import hashlib
import random
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from Response.models import User


def index(request):
    response = HttpResponse()
    response.content = '<h1>hello YY</h1>'
    response.write('<h1>you`re awesome!</h1>')
    response.charset = 'gb2312'
    response.flush()    # 清空缓冲区
    response.status_code = 404  # 欺骗爬虫
    return response


# 重定向
def redirect(request):
    if random.randrange(10) > 7:
        url = reverse('response:index')  # 反向解析
        return HttpResponseRedirect(url)
    return HttpResponse('you get')


# json
def json(request):
    data = {
        'status': 404,
        'msg': 'json',
    }
    return JsonResponse(data=data)


# 设置cookie
def set_cookie(request):
    response = HttpResponse('set success')
    response.set_signed_cookie('username', 'YY123', 'salt', max_age=60)
    return response


# 得到cookie
def get_cookie(request):
    username = request.get_signed_cookie('username', salt='salt')
    return HttpResponse(username)


# 例：（1）跳转登录页面
def login(request):
    return render(request, 'login.html')


# 例：（2）保存cookie
def save_cookie(request):
    username = request.POST.get('username')

    bytes_username = str(base64.b64encode(bytes(username, encoding='utf8')))
    b64_username = bytes_username[2:-1]

    response = HttpResponseRedirect(reverse('response:mine'))
    response.set_cookie('username', b64_username, max_age=60*60*24*1)
    return response


# 例：（3）个人页面
def mine(request):
    b64_username = request.COOKIES.get('username')
    username = base64.b64decode(b64_username).decode('utf-8')
    if username:
        path = reverse('response:logout')
        code = '''
            <a href=" '''+path+''' ">logout and delete cookie</a>
        '''
        return HttpResponse(username+code)
    return HttpResponseRedirect(reverse('response:login'))


# 例：（4）删除cookie
def logout(request):
    response = HttpResponseRedirect(reverse('response:login'))
    response.delete_cookie('username')
    return response


# session-login
def s_login(request):
    if request.method == 'GET':
        return render(request, 's_login.html')
    username = request.POST.get('username')
    request.session['username'] = username
    return HttpResponseRedirect(reverse('response:s_mine'))


# session-mine
def s_mine(request):
    username = request.session.get('username')
    code = '''
        <a href=" '''+reverse('response:s_logout')+''' ">out session</a>
    '''
    if username is None:
        return HttpResponse(username)
    return HttpResponse(username+code)


# session-delete
def s_logout(request):
    response = HttpResponseRedirect(reverse('response:s_mine'))
    # response.delete_cookie('sessionid')
    # del request.session['username']
    # 一起删，只删一个会出现“脏数据”
    request.session.flush()
    return response


# token
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User()
        user.u_name = username
        user.u_password = password
        user.save()
    except Exception as e:
        return HttpResponseRedirect(reverse('response:register'))
    return HttpResponseRedirect(reverse('response:t_login'))


def t_login(request):
    def generate_token(uname):
        register_time = time.ctime()
        return hashlib.new('md5', (register_time + uname).encode('utf-8')).hexdigest()

    if request.method == 'GET':
        return render(request, 't_login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.filter(u_name=username).filter(u_password=password)
    try:
        user = user.first()
        token = generate_token(username)
        user.u_token = token
        user.save()
        code = token+'''
            <br>
            <a href="'''+reverse('response:t_mine', args=(token,))+'''">mine args</a>
        '''
        response = HttpResponse(content=code)
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('response:t_login'))
    return response


def t_mine(request):
    token = request.GET.get('token')
    try:
        user = User.objects.get(u_token=token)
    except Exception as e:
        return HttpResponseRedirect(reverse('response:t_login'))
    data = {
        'username': user.u_name,
        'token': token,
    }
    return JsonResponse(data=data)

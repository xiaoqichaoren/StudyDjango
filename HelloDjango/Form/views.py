from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from Form.forms import LoginForm, UploadForm, RegisterForm
from Form.models import User


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():     # 若合法,将数据序列化到一个字典(form.cleaned_data)
            return HttpResponse('login success')
        return HttpResponse('failed')
    form = LoginForm()  # 实例化表单,渲染一个空表单
    return render(request, 'form_login.html', context=locals())


def upload(request):
    if request.method == 'POST':
        # 不能单独上传文件，必须包含其他字段(通过隐藏字段可以单独上传文件)
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('file')
            with open('/home/yy/DjangoProjects/HelloDjango/static/files/file.txt', 'wb+') as f:
                for part in file.chunks():
                    f.write(part)
                    f.flush()
            return HttpResponse('success')
        return HttpResponse('error')
    form = UploadForm()
    return render(request, 'upload.html', context=locals())


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User()
            u_id = form.cleaned_data.get('u_id')
            u_name = form.cleaned_data.get('u_name')
            u_password = form.cleaned_data.get('u_password')
            u_icon = form.cleaned_data.get('u_icon')
            user.u_id = u_id
            user.u_name = u_name
            user.u_password = u_password
            user.u_icon = u_icon
            user.save()
            return HttpResponse('已成功注册')
        return HttpResponse('注册失败')
    form = RegisterForm()
    return render(request, 'real_register.html', context=locals())

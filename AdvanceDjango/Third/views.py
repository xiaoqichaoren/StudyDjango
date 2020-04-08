from io import BytesIO

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from Third.models import People
from Third.utils import DrawVerify


def paginator(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 10))
    peoples = People.objects.all()

    paginator = Paginator(peoples, per_page)    # 将Queryset数据转换为分页器对象

    page_object = paginator.page(page)  # 将指定页面数据取出来，作为一个分页器对象
    return render(request, 'paginator.html', context=locals())


def yanzheng(request):
    # 默认size=(200, 100), mode='RGB', font_path=settings.FONT_PATH
    # 实例化一个绘制对象
    verify = DrawVerify()
    code = verify.Do()  # 绘制出图片
    # 抽取出图片对象
    image = verify.image
    fp = BytesIO()  # 实例化一个内存的IO流
    image.save(fp, 'png')   # 将图片对象存到内存流中
    # 往session中存验证码
    request.session['verify_code'] = code
    return HttpResponse(fp.getvalue(), content_type='image/png')


def login(request):
    if request.method == 'POST':
        yanzheng = request.POST.get('yanzheng')
        verify_code = request.session.get('verify_code')
        print(verify_code, yanzheng)
        if yanzheng == verify_code:
            return HttpResponse('正确')
        return HttpResponse('验证码错误')
    return render(request, 'yanzheng.html')

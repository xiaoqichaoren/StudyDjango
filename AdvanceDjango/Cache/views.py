from time import sleep

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.cache import cache_page


def index(request):
    return HttpResponse('Cache')


@cache_page(30, cache='default')
def db(request):
    data = '这是views中渲染到模板中的data'
    sleep(2)
    return render(request, 'info.html', context=locals())


# 自定义的缓存，使用起来和装饰器的效果一样
def custom(request):
    result = cache['default'].get('custom')
    if result:
        return HttpResponse(result)
    data = '这是custom的data'
    sleep(2)
    response = render(request, 'info.html', context=locals())
    cache.set('custom', response.content, timeout=30)
    return response


@cache_page(30, cache='redis')     # 只是更改了缓存方式，cache不需要重新设置
def redis(request):
    data = 'redis缓存页面'
    sleep(2)
    return render(request, 'info.html', context=locals())

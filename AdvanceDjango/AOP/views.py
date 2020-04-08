import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('这是aop的index')


def choujiang(request):
    if random.randrange(100) > 95:
        return HttpResponse('抢到了')
    return HttpResponse('没抢到')


def heibai(request):
    return HttpResponse('你在白名单')


def search(request):
    return HttpResponse('这是你搜索的')

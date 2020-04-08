import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        # print(ip, path)

        # 频率控制算法
        if path == '/aop/search/':
            now = time.time()
            result = cache.get(ip, default=[])  # 默认给一个空列表到缓存

            # 判断过程
            # 若存在缓存,且最后一个与最新的相差超过60s。则pop出去
            while result and now - result[-1] > 60:
                result.pop()
            # 若当前列表有10/10+个，直接不能查
            if len(result) >= 10:
                return HttpResponse('请求过于频繁,或者给爬虫返回一个虚假页面')

            # 操作过程
            # 将当前时间戳插入到列表头
            result.insert(0, now)
            cache.set(ip, result, timeout=60)  # 过期时间相当于最新的时间戳基础上+60s

        if path == '/aop/choujiang/':
            if ip == '127.0.0.1':
                if random.randrange(100) > 30:
                    return HttpResponse('NB')

        if path == '/aop/heibai/':
            if ip == '127.0.0.1':
                return HttpResponse('你在黑名单')

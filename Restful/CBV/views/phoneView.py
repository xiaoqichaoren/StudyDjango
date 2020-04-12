from django.http import HttpResponse
from django.views import View


class Phone(View):
    def get(self, request):
        print('获取所有')
        return HttpResponse('这是GET方法')

    def post(self, request):
        print('添加')
        return HttpResponse('这是POST方法')

    def put(self, request):
        print('修改')
        return HttpResponse('这是PUT方法')

    def delete(self, request):
        print('删除')
        return HttpResponse('这是delete方法')

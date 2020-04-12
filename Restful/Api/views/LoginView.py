from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Api.forms.LoginForm import LoginForm
from Api.models.LoginModel import LoginModel


@csrf_exempt
def login(request):
    # login函数是用接口调用的，在html中定义为POST方法即可，不需要再判断请求方式
    form = LoginForm(request.POST)
    if form.is_valid():
        try:
            model = LoginModel.objects.get(u_name=form.cleaned_data['u_name'])
        except Exception:
            return JsonResponse(data={'status': 404, 'msg': '用户不存在'})
        if model.u_password == form.cleaned_data['u_password']:
            data = {
                'status': 200,
                'msg': '成功登陆',
                'data': model.to_dict(),
            }
            return JsonResponse(data=data)
        return JsonResponse(data={'status': 400, 'msg': '密码错误'})
    return JsonResponse(data={'status': 403, 'msg': '用户名或密码非法'})

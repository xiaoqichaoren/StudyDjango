
from django.urls import path

from Third import views, tests

urlpatterns = [
    path('paginator/', views.paginator, name='paginator'),
    # 生成验证码
    path('yanzheng/', views.yanzheng, name='yanzheng'),
    path('login/', views.login, name='login'),
]

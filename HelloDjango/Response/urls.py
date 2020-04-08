from django.urls import path, re_path

from Response import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # 重定向
    path('redirect/', views.redirect, name='redirect'),
    # json
    path('json/', views.json, name='json'),
    # cookie
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    # 利用cookie登录
    path('login/', views.login, name='login'),
    path('save_cookie/', views.save_cookie, name='save_cookie'),
    path('mine/', views.mine, name='mine'),
    path('logout/', views.logout, name='logout'),
    # session
    path('s_login/', views.s_login, name='s_login'),
    path('s_mine/', views.s_mine, name='s_mine'),
    path('s_logout/', views.s_logout, name='s_logout'),
    # token
    path('register/', views.register, name='register'),
    path('t_login/', views.t_login, name='t_login'),
    # re_path(r'^t_mine/\?token=(.*.)', views.t_mine, name='t_mine'),
    path('t_mine/', views.t_mine, name='t_mine'),
]

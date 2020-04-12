from django.urls import path, re_path

from Api import views

urlpatterns = [
    # GET：查；POST：添加。这两种情况需设置book_id为0（表中没有id=0的字段）
    # PUT：更新；DELETE：删除
    re_path(r'^book/(?P<book_id>\d+)/', views.book),
    # 加上表单类
    path('login/', views.login),
]

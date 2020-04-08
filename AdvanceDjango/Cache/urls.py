from django.urls import path

from Cache import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # 库缓存
    path('db/', views.db, name='db'),
    # 自定义缓存
    path('custom/', views.custom, name='custom'),
    # 内存数据库
    path('redis/', views.redis),
]

from django.urls import path

from Form import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),

    # 用户注册
    path('register/', views.register, name='register'),
]

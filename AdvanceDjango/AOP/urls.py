from django.urls import path

from AOP import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('choujiang/', views.choujiang),
    path('heibai/', views.heibai),
    path('search/', views.search),
]

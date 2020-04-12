from django.urls import path

from CBV import views

urlpatterns = [
    path('phones/', views.Phone.as_view()),
]

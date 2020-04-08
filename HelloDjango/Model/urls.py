from django.urls import path

from Model import views

urlpatterns = [
    # 1:1
    path('add_student/', views.add_student, name='add_student'),
    path('add_card/', views.add_card, name='add_card'),
    path('remove_student/', views.remove_student, name='remove_student'),
    path('get_student/', views.get_student, name='get_student'),
    # M:N
    path('add_class/', views.add_class, name='add_class'),
    path('student_class/', views.student_class, name='student_class'),
    # extend(F_Key)
    path('add_fresh/', views.add_fresh, name='add_fresh'),
]

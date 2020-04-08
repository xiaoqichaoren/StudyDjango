from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from Model.models import Student, Card, Class, Fresh


def add_student(request):
    p_name = request.GET.get('p_name')
    student = Student()
    student.p_name = p_name
    student.save()
    return HttpResponse('add student success')


def add_card(request):
    id_num = request.GET.get('id_num')
    student = Student.objects.last()
    card = Card()
    card.id_num = id_num
    card.id_stu = student
    card.save()
    return HttpResponse('add card success')


def remove_student(request):
    student = Student.objects.last()
    student.delete()
    return HttpResponse('remove success')


def get_student(request):
    id_num = request.GET.get('id_num')
    card = Card.objects.get(id_num=id_num)
    student = card.id_stu
    return HttpResponse(student.p_name)


def add_class(request):
    c_name = request.GET.get('c_name')
    class_ = Class()
    class_.c_name = c_name
    class_.save()
    return HttpResponse('add success')


def student_class(request):
    p_name = request.GET.get('p_name')
    c_name = request.GET.get('c_name')
    class_ = Class.objects.get(c_name=c_name)
    student = Student.objects.get(p_name=p_name)
    class_.c_student.add(student)
    return HttpResponse(class_.c_name+'---'+student.p_name)


def add_fresh(request):
    f_department = request.GET.get('f_depart')
    fresh = Fresh()
    fresh.p_name = 'fresh'
    fresh.f_department = f_department
    fresh.save()
    return HttpResponse(fresh.p_name+'---'+fresh.f_department)
